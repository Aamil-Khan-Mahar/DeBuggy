'''
This Contains the Finder LLM Model for the project.

Task: This model is used to find the code file names from the code file descriptions. 
That are provided by the MappingLLM model.
Model: OpenAI GPT-4
Output: JSON Object with only the code file names.
'''

# Dependencies
import os
import dotenv
from openai import OpenAI
import json
from json import loads, dumps

# Model Class
class FinderLLM():
    def __init__(self, choice = 'GPT-4'):
        self.API_KEY = None
        self.model = None
        self.choice = choice
        if self.choice == 'GPT-4':
            self.API_KEY = dotenv.get_key('.env', 'OPENAI_API_KEY')
            self.model = OpenAI(api_key = self.API_KEY)
        self.prompt = """
        You are provided a bug report that was received from a user and a JSON object that contains the code file descriptions. 
        You are to provide the code file name that is the best match for the bug report.
        
        <bug_report>
        {bug_report}
        </bug_report>
        
        <code_mappings>
        {code_mappings}
        </code_mappings>
        
        -- Expected Response --
        JSON Object:
        Level 1 Fields: Filename, Reasoning, Confidence
        -- End of Expected Response --

        Response:
        """
        self.response = None
        self.bug_report = None
        self.code_mappings = None
        
    def set_code_mappings(self, code_mappings):
        self.code_mappings = code_mappings
        
    def find_code_filename(self, bug_report):
        self.bug_report = bug_report
        # try:
        #     if self.choice == 'GPT-4':
        #         self.response = self.model.chat.completions.create(
        #             model = 'gpt-4',
        #             messages = [
        #                 {
        #                     'role': 'system',
        #                     'content': 'You are a helpful AI'
        #                 },
        #                 {
        #                     'role': 'user',
        #                     'content': self.prompt.format(bug_report = self.bug_report, code_mappings = self.code_mappings)
        #                 }
        #             ]
        #         )
        #         return loads(self.response.choices[0].message.content)
        #         # return self.response.choices[0].message.content
        # except:
        #     print(f'Error in Finding')
        #     return 'Error in Finding'
        return {'Finding': 'Imagine this is the response from the model.'}
        
    def get_last_response(self):
        # return loads(self.response.choices[0].message.content)
        # return self.response.choices[0].message.content
        return {'Finding': 'Imagine this is the response from the model.'}