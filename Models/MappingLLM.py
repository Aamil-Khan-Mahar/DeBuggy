'''
This Contains the Mapping LLM Model for the project.

Task: This model is used to map the code files name to code file descriptions.
Model: OpenAI GPT-4
Output: JSON Object with all function names and their descriptions.
'''

# Dependencies
import os
import dotenv
from openai import OpenAI
from json import loads, dumps

# Model Class
class MappingLLM():
    def __init__(self, choice = 'GPT-4'):
        self.API_KEY = None
        self.model = None
        self.choice = choice
        if self.choice == 'GPT-4':
            self.API_KEY = dotenv.get_key('.env', 'OPENAI_API_KEY')
            self.model = OpenAI(api_key = self.API_KEY)
        self.prompt = """
        You are to provide a general description of a code file to be used as a mapping for the code file name.
        I've provided an example below here with the expected response format.
        
        --------- Example ----------
    
        -- Code --
        # filename: example.py
        
        Class Math():
            def __init__(self):
                pass
            
            def add(self, a, b):
                return a + b
            
            def subtract(self, a, b):
                return a - b
        -- End of Code --
        
        -- Expected Response --
        JSON Object:
        Level 1 Fields: File Name (EXACT NAME NOTHING ELSE), Description, Variables (Internal JSON Object NOT ARRAY), Functions (Internal JSON Object NOT ARRAY), Classes (Internal JSON Object NOT ARRAY)
        Level 2 Fields: Variable Name (Internal JSON Object), Function Name (Internal JSON Object), Class Name (Internal JSON Object)
        Level 3 Fields For Variables: Description, Type, Value, Scope
        Level 3 Fields For Functions: Description, Parameters (Internal JSON Object), Return values (Internal JSON Object), Scope
        Level 4 Fields For Parameters of Functions: Name, Type, Description
        Level 4 Fields For Return Values of Functions: Name (Internal JSON Object)
        Level 5 Fields For Name of Return Values of Functions: Type, Description
        Level 3 Fields For Classes: Description, Methods (Internal JSON Object)
        Level 4 Fields For Methods: Description, Parameters (Interanal JSON Object), Return values (Internal JSON Object), Scope
        Level 5 Fields For Parameters of Methods: Name, Type, Description
        Level 5 Fields For Return Values of Methods: Name (Internal JSON Object)
        Level 6 Fields For Name of Return Values of Methods: Type, Description
        -- End of Expected Response --
        
        --------- End of Example ----------
        
        Please provide a description for the code given below and respond in the expected format (JSON Object).
        
        <Code>
        {Code}
        </Code>
        Response:
        """
        self.response = None
    
    def infer(self, code):
        # try:
        #     if self.choice == 'GPT-4':
        #         self.response = self.model.chat.completions.create(
        #             model = 'gpt-4',
        #             messages = [
        #                 {
        #                     'role': 'system',
        #                     'content': 'You are a helpful AI.'
        #                 },
        #                 {
        #                     'role': 'user',
        #                     'content': self.prompt.format(Code = code).strip()
        #                 }
        #             ]
        #         )
        #         return loads(self.response.choices[0].message.content)
        #         # return self.response.choices[0].message.content
        # except Exception as e:
        #     # print('Error in Mapping')
        #     return 'Error in Mapping'
        return {'Inference': 'Imagine this is the response from the model.'}
    
    def get_last_response(self):
        # return loads(self.response.choices[0].message.content)
        # return self.response.choices[0].message.content
        return {'Inference': 'Imagine this is the response from the model.'}