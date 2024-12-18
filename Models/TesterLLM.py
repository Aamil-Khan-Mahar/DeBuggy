"""
This Contains the Tester LLM Model for the project.

Task: This model is given the code file that is provided by the DebuggerLLM model and the bug report that was received from a user along with the code mappings that were provided by the MappingLLM model for the Correct Code. It also creates new code mapping first for the new code file that was received from the DebuggerLLM model, and then it compares the new code mappings with the existing code mappings to see if the workings of the code file have changed.
Model: OpenAI GPT-4o
Output: JSON Object
"""

# Dependencies
import os
import dotenv
from openai import OpenAI
import json
from json import loads, dumps
if __name__ == '__main__':
    import MappingLLM
else:
    from Models.MappingLLM import MappingLLM

# Model Class
class TesterLLM():
    def __init__(self, choice = 'GPT-4o'):
        self.API_KEY = None
        self.model = None
        self.choice = choice
        if self.choice == 'GPT-4o':
            self.API_KEY = dotenv.get_key('.env', 'OPENAI_API_KEY')
            self.model = OpenAI(api_key = self.API_KEY)
        self.prompt = """
        You are provided with 4 Objects: Bug Report, Code Mappings for the Correct Code, Code Mappings for the New Code, and the New Code File. Your task is to compare the Code Mappings for the Correct Code with the Code Mappings for the New Code to evaluate if the New Code File is Correct in terms of its workings.
        
        <bug_report>
        {bug_report}
        </bug_report>
        
        <code_mappings>
        {code_mappings}
        </code_mappings>
        
        <new_code_mappings>
        {new_code_mappings}
        </new_code_mappings>
        
        <new_code_file>
        {new_code_file}
        </new_code_file>
        
        -- Expected Response --
        DO NOT ADD ```json ... ``` around the response.
        JSON Object with the following key-value pair:
        'Evaluation': 'True' or 'False'
        'Reason': 'The reason for the evaluation.'
        -- End of Expected Response --
        
        Response:
        """
        self.response = None
        self.bug_report = None
        self.code_file = None
        self.code_mapping_old = None
        self.code_mapping_new = None
        
    def evaluate(self, bug_report, code_mapping, new_code_file):
        self.bug_report = bug_report
        self.code_mapping_old = code_mapping
        mappingLLM = MappingLLM()
        self.code_mapping_new = mappingLLM.infer(new_code_file)
        try:
            if self.choice == 'GPT-4o':
                self.response = self.model.chat.completions.create(
                    model = 'gpt-4o',
                    messages = [
                        {
                            'role': 'system',
                            'content': 'You are a helpful AI that is to evaluate the workings of the code file.'
                        },
                        {
                            'role': 'user',
                            'content': self.prompt.format(bug_report = self.bug_report, code_mappings = self.code_mapping_old, new_code_mappings = self.code_mapping_new, new_code_file = new_code_file)
                        }
                    ]
                )
                return loads(self.response.choices[0].message.content), self.code_mapping_new
        except Exception as e:
            print(f'Error in Evaluation: {e}')
            return 'Error in Evaluation'
        # return {'Evaluation': 'Imagine this is the response from the model.'}
        
    def get_last_response(self):
        return loads(self.response.choices[0].message.content), self.code_mapping_new
        # return {'Evaluation': 'Imagine this is the response from the model.'}