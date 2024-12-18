"""
This file contains the full pipeline for the project in a class-based format with split methods and detailed docstrings.
"""

# Models
from Models.MappingLLM import MappingLLM
from Models.FinderLLM import FinderLLM
from Models.DebuggerLLM import DebuggerLLM
from Models.TesterLLM import TesterLLM

# Dependencies
import time
import threading
import os
import json
import socket
import subprocess
import logging
from queue import Queue


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email and Slack Servers as threads using subprocess
class EmailServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.email_process = None

    def run(self):
        """
        Start the email server subprocess.
        """
        try:
            self.email_process = subprocess.Popen(["python", "Tools/Email.py"], stdout=subprocess.DEVNULL)
            self.email_process.wait()
        except Exception as e:
            logging.error(f"Error starting Email server: {e}")


class SlackServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.slack_process = None

    def run(self):
        """
        Start the Slack server subprocess.
        """
        try:
            self.slack_process = subprocess.Popen(["python", "Tools/Slack.py"], stdout=subprocess.DEVNULL)
            self.slack_process.wait()
        except Exception as e:
            logging.error(f"Error starting Slack server: {e}")


class CodeMappingManager:
    def __init__(self, buggy_code_dir="./Data/Buggy", correct_code_dir="./Data/Correct" ,mappings_file="./Json/CodeMappings.json", correct_mappings_file="./Json/CorrectCodeMappings.json"):
        self.buggy_code_dir = buggy_code_dir
        self.correct_code_dir = correct_code_dir
        self.mappings_file = mappings_file
        self.correct_mappings_file = correct_mappings_file
        self.code_mappings = {}
        self.code_file_names = set()
        self.correct_code_mappings = {}
        self.correct_code_file_names = set()
        self.mapping_model = MappingLLM()

    def fetch_code_mappings(self):
        """
        Load existing code mappings from the JSON file.
        """
        try:
            with open(self.mappings_file, "r") as json_file:
                self.code_mappings = json.load(json_file)
            self.code_file_names.update(self.code_mappings.keys())
            logging.info("Code Mappings Fetched.")
        except FileNotFoundError:
            self.code_mappings = {}
            logging.info(f"No existing code mappings found at {self.mappings_file}. Starting fresh.")

    def fetch_correct_code_mappings(self):
        """
        Load existing correct code mappings from the JSON file.
        """
        try:
            with open(self.correct_mappings_file, "r") as json_file:
                self.correct_code_mappings = json.load(json_file)
            self.correct_code_file_names.update(self.correct_code_mappings.keys())
            logging.info("Correct Code Mappings Fetched.")
        except FileNotFoundError:
            self.correct_code_mappings = {}
            logging.info(f"No existing code mappings found at {self.correct_mappings_file}. Starting fresh.")
            
    def check_code_mappings(self):
        """
        Check for unmapped files in the buggy code directory.
        :return: List of unmapped file names.
        """
        files = [f for f in os.listdir(self.buggy_code_dir) if f.endswith(".py") and f != "__init__.py"]
        return [filename for filename in files if filename not in self.code_file_names]

    def check_correct_code_mappings(self):
        """
        Check for unmapped files in the correct code directory.
        :return: List of unmapped file names.
        """
        files = [f for f in os.listdir(self.correct_code_dir) if f.endswith(".py") and f != "__init__.py"]
        return [filename for filename in files if filename not in self.correct_code_file_names]
    
    def update_code_mappings(self, unmapped_files):
        """
        Update the code mappings for newly discovered unmapped files.
        """
        for filename in unmapped_files:
            file_path = os.path.join(self.buggy_code_dir, filename)
            try:
                with open(file_path, "r") as file:
                    code = file.read()
                logging.info(f"Mapping {filename}...")
                response = self.mapping_model.infer(code)
                if response != "Error in Mapping":
                    self.code_mappings[filename] = response
                    self.code_file_names.add(filename)
                else:
                    logging.error(f"Error mapping {filename}")
            except Exception as e:
                logging.error(f"Error reading or mapping {filename}: {e}")
        self.save_mappings()
        
    def update_correct_code_mappings(self, unmapped_files):
        """
        Update the correct code mappings for newly discovered unmapped files.
        """
        for filename in unmapped_files:
            file_path = os.path.join(self.correct_code_dir, filename)
            try:
                with open(file_path, "r") as file:
                    code = file.read()
                logging.info(f"Mapping {filename}...")
                response = self.mapping_model.infer(code)
                if response != "Error in Mapping":
                    self.correct_code_mappings[filename] = response
                    self.correct_code_file_names.add(filename)
                else:
                    logging.error(f"Error mapping {filename}")
            except Exception as e:
                logging.error(f"Error reading or mapping {filename}: {e}")
        self.save_correct_mappings()

    def save_mappings(self):
        """
        Save the updated code mappings back to the JSON file.
        """
        try:
            with open(self.mappings_file, "w") as json_file:
                json.dump(self.code_mappings, json_file, indent=4)
            logging.info("Code Mappings Saved.")
        except Exception as e:
            logging.error(f"Error saving code mappings: {e}")
            
    def save_correct_mappings(self):
        """
        Save the updated correct code mappings back to the JSON file.
        """
        try:
            with open(self.correct_mappings_file, "w") as json_file:
                json.dump(self.correct_code_mappings, json_file, indent=4)
            logging.info("Correct Code Mappings Saved.")
        except Exception as e:
            logging.error(f"Error saving correct code mappings: {e}")


class BugReportServer(threading.Thread):
    def __init__(self, email_port=4091, slack_port=4090):
        super().__init__()
        self.email_port = email_port
        self.slack_port = slack_port
        self.email_socket = None
        self.slack_socket = None
        self.slack_reports = Queue()
        self.email_reports = Queue()
        self.slack_report_ids = set()
        self.email_report_ids = set()
        self.lock = threading.Lock()

    def setup_socket(self, port):
        """
        Configures a socket to listen for incoming connections.
        :param port: The port on which the socket should listen.
        :return: The configured socket object.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("127.0.0.1", port))
            sock.listen(5)
            logging.info(f"Socket listening on port {port}!")
            return sock
        except Exception as e:
            logging.error(f"Error setting up socket on port {port}: {e}")
            return None

    def handle_connections(self, sock, report_storage, report_ids):
        """
        Handles incoming connections for a given socket.
        """
        if not sock:
            logging.warning("Socket is not initialized; skipping connection handling.")
            return

        while True:
            try:
                client_socket, _ = sock.accept()
                data = client_socket.recv(1024).decode()
                self.process_report(data, report_storage, report_ids)
                client_socket.close()
            except Exception as e:
                logging.error(f"Error during connection handling: {e}")

    def process_report(self, report_data, report_storage, report_ids):
        """
        Processes incoming report data.
        """
        try:
            reports = json.loads(report_data)
            with self.lock:
                for report in reports.get("reports", []):
                    report_id = report.get("reportID")
                    if report_id and report_id not in report_ids:
                        report_storage.put(report)
                        report_ids.add(report_id)
                        logging.info(f"Processed report: {report_id}")
                    else:
                        logging.warning(f"Duplicate or invalid report: {report_id}")
        except Exception as e:
            logging.error(f"Error processing report: {e}")

    def run(self):
        """
        Starts the BugReportServer threads for handling email and Slack connections.
        """
        self.email_socket = self.setup_socket(self.email_port)
        self.slack_socket = self.setup_socket(self.slack_port)

        if self.email_socket:
            email_thread = threading.Thread(target=self.handle_connections, args=(self.email_socket, self.email_reports, self.email_report_ids))
            email_thread.start()
        else:
            logging.error("Email server setup failed; skipping.")

        if self.slack_socket:
            slack_thread = threading.Thread(target=self.handle_connections, args=(self.slack_socket, self.slack_reports, self.slack_report_ids))
            slack_thread.start()
        else:
            logging.error("Slack server setup failed; skipping.")


class ReportResolver(threading.Thread):
    def __init__(self, bug_server, code_mapping_manager):
        super().__init__()
        self.bug_server = bug_server
        self.code_mapping_manager = code_mapping_manager
        self.finder_model = FinderLLM()
        self.debugger_model = DebuggerLLM()
        self.tester_model = TesterLLM()
        self.resolved_reports = {}

    def resolve_reports(self):
        """
        Periodically resolve bug reports using FinderLLM and DebuggerLLM.
        """
        while True:
            reports = []
            while not self.bug_server.email_reports.empty():
                reports.append(self.bug_server.email_reports.get())
            while not self.bug_server.slack_reports.empty():
                reports.append(self.bug_server.slack_reports.get())
            updated = False
            for report in reports:
                start_time = time.time()
                report_id = report['reportID']
                bug_report = report['text']
                code_mapping = self.code_mapping_manager.code_mappings
                correct_code_mapping = self.code_mapping_manager.correct_code_mappings
                try:
                    logging.info(f'Resolving bug report {report_id}...')
                    self.finder_model.set_code_mappings(code_mapping)
                    code_filename = self.finder_model.find_code_filename(bug_report)
                    code_file = ''
                    if 'Finding' in code_filename.keys():
                        logging.error(f"FinderLLM Commented out")
                        continue
                    elif code_filename['Filename'] not in os.listdir("./Data/Buggy"):
                        logging.error(f"Code file {code_filename['Filename']} not found.")
                        continue
                    else:
                        logging.info(f"Code file found: {code_filename['Filename']}")
                        with open(f"./Data/Buggy/{code_filename['Filename']}", "r") as file:
                            code_file = file.read()
                    debugged_code = self.debugger_model.debug(bug_report, code_file)
                    if 'Debugging' in debugged_code.keys():
                        logging.error(f"DebuggerLLM Commented out")
                        continue
                    elif 'Corrected_code_file' in debugged_code.keys():
                        Resolved = False
                        tries = 0
                        efforts = {}
                        while not Resolved and tries < 3:
                            response, new_code_mapping = self.tester_model.evaluate(bug_report, correct_code_mapping[code_filename['Filename'].replace('Buggy', 'Correct')], debugged_code['Corrected_code_file'])
                            efforts['Try ' + str(tries + 1)] = { 'Evaluation': response['Evaluation'], 'Reason': response['Reason'] , 'Code': debugged_code['Corrected_code_file']}
                            if 'true' in response['Evaluation'].lower():
                                Resolved = True
                                self.code_mapping_manager.code_mappings[code_filename['Filename']] = new_code_mapping
                                self.code_mapping_manager.save_mappings()
                            else:
                                if tries == 2:
                                    continue 
                                debugged_code = self.debugger_model.debug(bug_report, debugged_code['Corrected_code_file'])
                                tries += 1
                        resolved_report = {
                            'status': 'Resolved' if Resolved else 'Unresolved',
                            'evaluation_reason': response['Reason'],
                            'efforts': efforts,
                            'tries': tries,
                            'reportID': report_id,
                            'bug_report': bug_report,
                            'code_file': code_file,
                            'debugged_code': debugged_code['Corrected_code_file'],
                            'reasoning': code_filename['Reasoning'],
                            'confidence': code_filename['Confidence'],
                            'start_time': start_time,
                            'end_time': time.time(),
                            'reporting_time': report['timestamp']
                        }
                        if Resolved:
                            logging.info(f"Resolved {report_id} successfully. Changing code file {code_filename['Filename']}")
                            with open(f"./Data/Buggy/{code_filename['Filename']}", "w") as file:
                                file.write(debugged_code['Corrected_code_file'])
                        else:
                            logging.error(f"Failed to resolve {report_id}.")
                        with self.bug_server.lock:
                            self.resolved_reports[report_id] = resolved_report
                        updated = True
                except Exception as e:
                    logging.error(f"Error resolving report {report_id}: {e}")
            if updated:
                self.save_resolved_reports()
            updated = False
            time.sleep(10)
    
    def save_resolved_reports(self):
        """
        Save the resolved reports to a JSON file.
        """
        try:
            with open("./Json/ResolvedReports.json", "w") as json_file:
                json.dump(self.resolved_reports, json_file, indent=4)
            logging.info("Resolved Reports Saved.")
        except Exception as e:
            logging.error(f"Error saving resolved reports: {e}")
            
    def fetch_resolved_reports(self):
        """
        Load existing resolved reports from the JSON file.
        """
        try:
            with open("./Json/ResolvedReports.json", "r") as json_file:
                self.resolved_reports = json.load(json_file)
            logging.info("Resolved Reports Fetched.")
        except FileNotFoundError:
            self.resolved_reports = {}
            logging.info("No existing resolved reports found. Starting fresh.")

    def run(self):
        """
        Start the report resolver thread.
        """
        self.fetch_resolved_reports()
        self.resolve_reports()

if __name__ == "__main__":
    email_server = EmailServer()
    slack_server = SlackServer()
    email_server.start()
    slack_server.start()

    code_mapping_manager = CodeMappingManager()
    bug_server = BugReportServer()
    resolver = ReportResolver(bug_server, code_mapping_manager)

    code_mapping_manager.fetch_code_mappings()
    code_mapping_manager.fetch_correct_code_mappings()
    unmapped_files = code_mapping_manager.check_code_mappings()
    correct_unmapped_files = code_mapping_manager.check_correct_code_mappings()
    code_mapping_manager.update_code_mappings(unmapped_files)
    code_mapping_manager.update_correct_code_mappings(correct_unmapped_files)
    bug_server.start()
    resolver.start()

    email_server.join()
    slack_server.join()
    bug_server.join()
    resolver.join()