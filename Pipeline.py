'''
This File contains the full pipeline for the project. Combining all the models and the data fetching and preprocessing steps.
'''


from Models.MappingLLM import MappingLLM
print("MappingLLM Imported.")
from Models.FinderLLM import FinderLLM
print("FinderLLM Imported.")
from Models.DebuggerLLM import DebuggerLLM
print("DebuggerLLM Imported.")

# importing Tools
from Tools.Email import EmailListener
print("EmailListener Imported.")
from Tools.Slack import SlackListener
print("SlackListener Imported.")

# importing Libraries
import time
import threading
import dotenv
import os
import json
import subprocess
import argparse

# setting up the Models and Tools
mapping_model = MappingLLM()
finder_model = FinderLLM()
debugger_model = DebuggerLLM()
email_tool = EmailListener()
slack_tool = SlackListener() 

# Threads for the Tools
email_thread = threading.Thread(target=email_tool.connect) # Email Tool Thread
slack_thread = threading.Thread(target=slack_tool.start) # Slack Tool Thread

# CONSTANTS
global CODE_MAPPINGS, CODE_FILE_NAMES, BUG_REPORTS, REPORTS, REPORT_IDs # Global Variables
CODE_MAPPINGS = {} # Dictionary of all the Code Mappings
CODE_FILE_NAMES = set() # Set of all the Code File Names
BUG_REPORTS = [] # List of all the Bug Reports
REPORTS = {} # Dictionary of all the Reports
REPORT_IDs = set() # Set of all the Report IDs

def generate_REPORT_ID():
    global REPORT_IDs
    report_id = 1
    while report_id in REPORT_IDs:
        report_id += 1
    REPORT_IDs.add(report_id)
    return report_id

def fetch_code_mappings():
    global CODE_MAPPINGS
    global CODE_FILE_NAMES
    with open("./Json/CodeMappings.json", "r") as json_file:
        CODE_MAPPINGS = json.load(json_file)
    for code_file in CODE_MAPPINGS.keys():
        CODE_FILE_NAMES.add(code_file)
    print("Code Mappings Fetched.")

def check_and_update_code_mappings():
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
    print("Code Mappings Updated.")return {'Inference': 'Imagine this is the response from the model.'}
    
    # Saving the updated Code Mappings
    with open("./Json/CodeMappings.json", "w") as json_file:
        json.dump(CODE_MAPPINGS, json_file, indent=4)
    print("Code Mappings Saved.")
    print("Filnames:\n", sorted(CODE_FILE_NAMES))
    
fetch_code_mappings()
check_and_update_code_mappings()
