import time
import socket
import dotenv
from imap_tools import MailBox, AND
from json import dumps, loads

class EmailListener:
    def __init__(self, env_path: str = '../.env', folder: str = 'INBOX'):
        """
        Initialize the EmailListener class.

        :param env_path: Path to .env file for credentials
        :param folder: The folder to monitor for new emails. Default is 'INBOX'.
        """
        self.reports = []
        self.new_reports = []
        self.reportID = 1
        self.email = dotenv.get_key(env_path, 'EMAIL')
        self.password = dotenv.get_key(env_path, 'APP_PASS')
        self.folder = folder
        self.mailbox = None
        self.seen_uids = set()
    
    def connect(self):
        """
        Connect to the mailbox and start fetching emails.
        """
        try:
            self.mailbox = MailBox("imap.gmail.com").login(self.email, self.password, self.folder)
            print("Connected to mailbox.")
            while True:
                self.check_emails()
                time.sleep(15)
        except Exception as e:
            print(f"Error: {e}")
    
    def check_emails(self):
        """
        Check for new emails and save them if not already seen.
        """
        self.mailbox.folder.set(self.folder)
        for msg in self.mailbox.fetch(AND(seen=False)):
            if msg.uid in self.seen_uids:
                continue
            report = {
                'from': msg.from_,
                'subject': msg.subject,
                'text': msg.text,
                'reportID': f'Email-{self.reportID}',
                'timestamp': time.time()
            }
            self.reports.append(report)
            self.new_reports.append(report)
            self.seen_uids.add(msg.uid)
            self.reportID += 1
        if len(self.new_reports) > 0:
            self.send_reports_to_receiver()

    def send_reports_to_receiver(self):
        """
        Send the fetched reports to the receiver via the socket.
        """
        try:
            reports_data = {
                'reports': self.new_reports
            }
            reports_str = dumps(reports_data)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('127.0.0.1', 9001))
            self.socket.sendall(reports_str.encode())
            self.new_reports = []
            self.socket.close()
        except Exception as e:
            print(f"Error sending reports: {e}")
            
if __name__ == '__main__':
    email_listener = EmailListener()
    email_listener.connect()