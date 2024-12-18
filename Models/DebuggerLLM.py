"""
This Contains the Debugger LLM Model for the project.

Task: This model is used to debug the code files that are provided by the FinderLLM model.
Model: OpenAI GPT-4
Output: Correct code file with the bugs fixed comments above the lines that were fixed.
"""

# Dependencies
import os
import dotenv
from openai import OpenAI
import json
from json import loads, dumps

class DebuggerLLM():
    def __init__(self, choice = 'GPT-4'):
        self.API_KEY = None
        self.model = None
        self.choice = choice
        if self.choice == 'GPT-4':
            self.API_KEY = dotenv.get_key('.env', 'OPENAI_API_KEY')
            self.model = OpenAI(api_key = self.API_KEY)
        self.prompt = """
        You are to debug the code file that is given to you and the bug report that was received from a user.
        Please provide the code file with the bugs in the file fixed and comments above the lines that were fixed, telling what was fixed.
        Make sure to correct all bugs in the code file.
        
        -- Expected Response --
        Code File:
        # filename: Code1Buggy.py
        class Math():
            def __init__(self):
                pass
                
            def add(self, a, b):
                # Fixed the bug here by changing the operator from - to +
                return a + b
                
            # Fixed the bug here by changing parameter from aa to a 
            def subtract(self, a, b):
                return a - b
                
        -- End of Expected Response --
        
        <bug_report>
        {bug_report}
        </bug_report>
        
        <code_file>
        {code_file}
        </code_file>
        Response: JSON Object with the field 'Corrected_code_file'.
        """
        self.response = None
        self.bug_report = None
        self.code_file = None
        
    def debug(self, bug_report, code_file):
        self.bug_report = bug_report
        self.code_file = code_file
        # try:
        #     if self.choice == 'GPT-4':
        #         self.response = self.model.chat.completions.create(
        #             model = 'gpt-4',
        #             messages = [
        #                 {
        #                     'role': 'system',
        #                     'content': self.prompt.format(bug_report = self.bug_report, code_file = self.code_file)
        #                 }
        #             ]
        #         )
        #     # return loads(self.response.choices[0].message.content)
        #     return self.response.choices[0].message.content
        # except:
        #     print(f'Error in Debugging')
        #     return 'Error in Debugging'
        return {'Debugging': 'Imagine this is the response from the model.'}
        
    def get_last_response(self):
        # return loads(self.response.choices[0].message.content)
        # return self.response.choices[0].message.content
        return {'Inference': 'Imagine this is the response from the model.'}
        
        
# Test the DebuggerLLM model
if __name__ == '__main__':
    mappings = None
    with open('../Data/Json/mappings.json', 'r') as file:
        mappings = json.load(file)
    debugger = DebuggerLLM()
    finder = FinderLLM()
    finder.set_code_mappings(mappings)
    # bug_report = 'The add function is not working correctly.'
    bug_report = 'The student is not being added correctly.'
    code_file = 'Code1Buggy.py'
    code = finder.find_code_filename(bug_report)
    code_file = None
    with open(f'../Data/Buggy/{code['Filename']}', 'r') as file:
        code_file = file.read()
    response = debugger.debug(bug_report, code_file)
    print(response)