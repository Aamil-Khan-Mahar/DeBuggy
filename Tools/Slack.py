import os
import socket
import dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient
from json import dumps, loads
import time

class SlackListener:
    def __init__(self, env_path: str = "../.env", port: int = 8005):
        """
        Initialize the SlackListener.

        :param env_path: Path to the .env file containing Slack credentials.
        :param port: Port on which the Flask app runs. Default is 8000.
        """
        self.slack_token = dotenv.get_key(env_path, "SLACK_TOKEN")
        self.signing_secret = dotenv.get_key(env_path, "SLACK_SIGNING_SECRET")
        self.port = port
        self.reportID = int(dotenv.get_key(env_path, 'SLACK_REPORT_ID', default=1))
        if not self.slack_token or not self.signing_secret:
            raise ValueError("Slack credentials (SLACK_TOKEN or SLACK_SIGNING_SECRET) are missing.")
        self.app = Flask(__name__)
        self.slack_event_adapter = SlackEventAdapter(self.signing_secret, "/slack/events", self.app)
        self.client = WebClient(token=self.slack_token)
        self.bot_id = self.client.api_call("auth.test")['user_id']
        self.report_channel_id = 'C085V73MD97'
        self.reports = []
        self.new_reports = []
        # Event listener for Slack messages
        self.slack_event_adapter.on("message")(self.handle_message)

    def handle_message(self, payload):
        """
        Handle incoming message events.

        :param payload: Event payload from Slack.
        """
        event = payload.get("event", {})
        channel_id = event.get("channel")
        user_id = event.get("user")
        text = event.get("text")
        # Only process messages from the #report channel
        if user_id != self.bot_id and channel_id == self.report_channel_id:
            report = {
                "user_id": user_id, 
                "channel_id": channel_id, 
                "text": text,
                "reportID": f"Slack-{self.reportID}",
                "timestamp": time.time()
            }
            self.reports.append(report)
            self.new_reports.append(report)
            self.reportID += 1
            dotenv.set_key('.env', 'SLACK_REPORT_ID', str(self.reportID))
            
    def get_messages(self):
        """
        Retrieve all new messages received so far.

        :return: List of new messages.
        """
        new_reports = self.new_reports
        self.new_reports = []
        return new_reports

    def send_reports_to_receiver(self):
        """
        Send the new Slack reports to the receiver via a socket.
        """
        try:
            reports_data = {
                'reports': self.new_reports
            }
            reports_str = dumps(reports_data)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('127.0.0.1', 9002))
            client_socket.sendall(reports_str.encode())  
            self.new_reports = []
            client_socket.close()  
        except Exception as e:
            print(f"Error sending reports: {e}")
    
    def start(self, debug=False):
        """
        Start the Slack listener.

        This method starts the Flask app and begins listening for Slack events.
        It also periodically sends new reports to the receiver.
        """
        print("Slack listener is running...")
        from threading import Thread
        flask_thread = Thread(target=self.app.run, kwargs={'debug': debug, 'port': self.port})
        flask_thread.start()
        while True:
            if len(self.new_reports) > 0:
                self.send_reports_to_receiver()
            time.sleep(5)
            
if __name__ == '__main__':
    slack_listener = SlackListener(env_path='.env')
    slack_listener.start()