'''
This File contains the full pipeline for the project.
'''

# importing Models
from Models.MappingLLM import MappingLLM
from Models.FinderLLM import FinderLLM
from Models.DebuggerLLM import DebuggerLLM

# importing Libraries
import time
import threading
import dotenv
import os
import json
import subprocess
import argparse
from multiprocessing import Process
import socket

# Socket as a Receiver
email_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
slack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting up the Models
mapping_model = MappingLLM()
finder_model = FinderLLM()
debugger_model = DebuggerLLM()

# CONSTANTS
global CODE_MAPPINGS, CODE_FILE_NAMES, BUG_REPORTS, SLACK_REPORTS, EMAIL_REPORTS, SLACK_REPORT_IDs, EMAIL_REPORT_IDs 
CODE_MAPPINGS = {}
CODE_FILE_NAMES = set()
BUG_REPORTS = []
SLACK_REPORTS = {}
EMAIL_REPORTS = {}
SLACK_REPORT_IDs = set()
EMAIL_REPORT_IDs = set()

# Functions for Code Mappings
def fetch_code_mappings():
    '''
    Fetches the Code Mappings from the Json file.
    '''
    global CODE_MAPPINGS
    global CODE_FILE_NAMES
    with open("./Json/CodeMappings.json", "r") as json_file:
        CODE_MAPPINGS = json.load(json_file)
    for code_file in CODE_MAPPINGS.keys():
        CODE_FILE_NAMES.add(code_file)
    print("Code Mappings Fetched.")

def check_and_update_code_mappings():
    '''
    Checks if the Code Mappings are updated (Just makes sure all files are included) or not.
    If not, then updates the Code Mappings.
    '''
    global CODE_MAPPINGS
    global CODE_FILE_NAMES
    files = os.listdir("./Data/Buggy")
    files = [file for file in files if file.endswith(".py")]
    for filename in files:
        if filename not in CODE_FILE_NAMES and filename != '__init__.py':
            with open(f"./Data/Buggy/{filename}", "r") as file:
                code = file.read()
                print(f'adding {filename}\'s mapping')
                response = mapping_model.infer(code)
                if response != 'Error in Mapping':
                    CODE_MAPPINGS[filename] = response
                    CODE_FILE_NAMES.add(filename)
                else:
                    print(f"Error in Mapping: {filename}")
    print("Code Mappings Updated.")
    with open("./Json/CodeMappings.json", "w") as json_file:
        json.dump(CODE_MAPPINGS, json_file, indent=4)
    print("Code Mappings Saved.")
    print("Filenames:\n", sorted(CODE_FILE_NAMES))

# Functions for Bug Reports - Socket Programming
def setup_email_socket():
    '''
    Sets up the Email Socket for receiving the Email Reports.
    '''
    try:
        email_socket.bind(('127.0.0.1', 9001))  
        email_socket.listen(5)
        print("Email Socket Started!")
    except Exception as e:
        print(f"Error setting up Email socket: {e}")

def setup_slack_socket():
    '''
    Sets up the Slack Socket for receiving the Slack Reports.
    '''
    try:
        slack_socket.bind(('127.0.0.1', 9002))
        slack_socket.listen(5)
        print("Slack socket listening on port 9002!")
    except Exception as e:
        print(f"Error setting up Slack socket: {e}")

def handle_incoming_email_connections():
    '''
    Handles the incoming Email Connections.
    Sends the Email Reports to the receive_report function.
    '''
    while True:
        client_socket, client_address = email_socket.accept()
        email_data = client_socket.recv(1024).decode()
        receive_report(email_data)
        client_socket.close()

def handle_incoming_slack_connections():
    '''
    Handles the incoming Slack Connections.
    Sends the Slack Reports to the receive_report function.
    '''
    while True:
        client_socket, client_address = slack_socket.accept()
        slack_data = client_socket.recv(1024).decode()
        receive_report(slack_data)
        client_socket.close()

def receive_report(report_data):
    """
    Adds the received report(s) to the appropriate dictionary (email or slack).
    :param report_data: JSON string containing report(s) to be processed Key: reports, Value: List of reports
    """
    try:
        reports = json.loads(report_data)
        for report in reports['reports']:
            reportID = report['reportID']
            if reportID not in SLACK_REPORT_IDs and reportID not in EMAIL_REPORT_IDs:
                if 'from' in report:
                    EMAIL_REPORTS[reportID] = report
                    EMAIL_REPORT_IDs.add(reportID)
                    print(f"Processing email report: {reportID}")
                elif 'user_id' in report:
                    SLACK_REPORTS[reportID] = report
                    SLACK_REPORT_IDs.add(reportID)
                    print(f"Processing slack report: {reportID}")
                else:
                    print(f"Invalid report")
            else:
                print(f"ReportID already processed: {reportID}")
    except Exception as e:
        print(f"Error processing report: {e}")
        
def start_email_server():
    '''
    Starts the Email Server.
    '''
    setup_email_socket()
    handle_incoming_email_connections()

def start_slack_server():
    '''
    Starts the Slack Server.
    '''
    setup_slack_socket()
    handle_incoming_slack_connections()

if __name__ == "__main__":
    email_thread = threading.Thread(target=start_email_server)
    slack_thread = threading.Thread(target=start_slack_server)
    email_thread.start()
    slack_thread.start()
    email_thread.join()
    slack_thread.join()