'''
This File contains the full pipeline for the project. Combining all the models and the data fetching and preprocessing steps.
'''

# Importing Models
from Models.DebuggerLLM import DebuggerLLM
from Models.FinderLLM import FinderLLM
from Models.IdentifierLLM import IdentifierLLM

# Importing Tools
from Tools.Email import Email
from Tools.Slack import Slack


# Datasets

BuggyCode = '../pytracebugs_dataset_v1/buggy_dataset/bugfixes_train.pickle'
StableCode = '../pytracebugs_dataset_v1/stable_dataset/stable_code_train.pickle'

# Reading the Pickle Files
import pickle
with open(BuggyCode, 'rb') as f:
    buggy_code = pickle.load(f)
    
with open(StableCode, 'rb') as f:
    stable_code = pickle.load(f)
    
