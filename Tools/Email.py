'''
This Contains the Email Tool for the project.
'''

import time
import dotenv
from imap_tools import MailBox, AND, OR, NOT


class EmailListener:
    def __init__(self, email: str = dotenv.get_key('.env', 'EMAIL'), password: str = dotenv.get_key('.env', 'APP_PASS'), folder: str = 'INBOX'):
        """
        Initialize the EmailListener class.

        :param email: The email address to connect to.
        :param password: The password for the email account (use app password if 2FA is enabled).
        :param folder: The folder to monitor for new emails. Default is 'INBOX'.
        :param check_interval: Time interval (in seconds) between checks for new emails.
        """
        self.reportID = 1
        self.reports = []
        self.new_reports = []
        self.email = email
        self.password = password
        self.folder = folder
        self.mailbox = None
        self.seen_uids = set()

    def connect(self):
        """Connect to the mailbox."""
        try:
            self.mailbox = MailBox("imap.gmail.com").login(self.email, self.password, self.folder)
            while True:
                self.check_emails()
                time.sleep(3)
        except Exception as e:
            print(f"Error: {e}")
            
    def check_emails(self):
        """Check for new emails and mark them seen and save the seen UIDs and subject and content as a Single String."""
        self.mailbox.folder.set(self.folder)
        for msg in self.mailbox.fetch(AND(seen=False)):
            if msg.uid in self.seen_uids:
                continue
            # print(f"New email from {msg.from_} : {msg.subject} : {msg.text}")
            report = {
                'from': msg.from_,
                'subject': msg.subject,
                'text': msg.text.replace('\n', ' '),
                'reportID': self.reportID,
            }
            self.reports.append(report)
            self.new_reports.append(report)
            self.seen_uids.add(msg.uid)
            self.reportID += 1
            
    def get_reports(self):
        """Return all the reports."""
        return self.reports
    
    def get_new_reports(self):
        """Return only the new reports."""
        new_reports = self.new_reports
        self.new_reports = []
        return new_reports

# Example usage
if __name__ == "__main__":
    listener = EmailListener() 
    listener.connect()