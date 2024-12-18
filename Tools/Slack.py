"""
This contains the code for fetching and handling data from Slack.
"""

import os
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient
from pathlib import Path
import dotenv


class SlackListener:
    def __init__(self, env_path: str = ".env", port: int = 8000):
        """
        Initialize the SlackListener.

        :param env_path: Path to the .env file containing Slack credentials.
        :param port: Port on which the Flask app runs. Default is 8000.
        """
        dotenv.load_dotenv(env_path)
        self.slack_token = os.getenv("SLACK_TOKEN")
        self.signing_secret = os.getenv("SLACK_SIGNING_SECRET")
        self.port = port
        if not self.slack_token or not self.signing_secret:
            raise ValueError("Slack credentials (SLACK_TOKEN or SLACK_SIGNING_SECRET) are missing.")
        self.app = Flask(__name__)
        self.slack_event_adapter = SlackEventAdapter(self.signing_secret, "/slack/events", self.app)
        self.client = WebClient(token=self.slack_token)
        self.bot_id = self.client.api_call("auth.test")['user_id']
        self.report_channel_id = 'C085V73MD97'
        self.reports = []
        self.new_reports = []
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
        if user_id != self.bot_id and channel_id == self.report_channel_id:
            self.reports.append({"user_id": user_id, "channel_id": channel_id, "text": text})
            print(f"Received message: {text} from user {user_id} in channel {channel_id}")

    def get_messages(self):
        """
        Retrieve all messages received so far.

        :return: List of messages.
        """
        return self.reports

    def start(self):
        """
        Start the Slack listener.

        This method starts the Flask app and begins listening for Slack events.
        """
        print("Slack listener is running...")
        self.app.run(debug=True, port=self.port)