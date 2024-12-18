# DeBuggy: An Automated Debugging Pipeline

## Contributors

```python
class Aamil_Khan_Mahar():
    def details(self):
        self.email = "25020240@lums.edu.pk"
        self.roll_number = "25020240"
        
class Abdullah_Anwar():
    def details(self):
        self.email = "25100214@lums.edu.pk"
        self.roll_number = "25100214"
        
class Saad_Liaquat():
    def details(self):
        self.email = "25100259@lums.edu.pk"
        self.roll_number = "25100259"
```

## Overview

The **Bug Report Resolution Pipeline** is an AI-powered system designed to handle, debug, and resolve bug reports related to code. This pipeline is built using a set of machine learning models and components to automate the process of mapping, debugging, and evaluating code to fix bugs. The system integrates with email and Slack servers to collect bug reports and uses AI models to identify the issues, debug the code, and verify the fixes.

### Core Features:
- **Bug Report Reception**: Listens for bug reports from email and Slack.
- **Code Mapping**: Automatically maps buggy code to its correct counterpart.
- **Automatic Debugging**: Uses an AI model to debug code according to bug reports.
- **Code Testing and Evaluation**: Verifies if the debugged code works correctly.
- **Reporting**: Logs the results of each bug report, including whether the issue was resolved or not.

## Project Structure

This project is organized into several classes that handle different parts of the pipeline:

1. **EmailServer** and **SlackServer**:
   - These are threaded classes that run subprocesses to listen for incoming bug reports from email and Slack.
   - They initiate communication with the system by setting up a socket server to listen on specified ports.

2. **BugReportServer**:
   - Manages incoming bug reports from both email and Slack. It stores the reports in separate queues and ensures they are processed by the system.

3. **CodeMappingManager**:
   - Manages code mappings between buggy and correct code. It loads existing mappings, checks for unmapped files, and updates mappings when new files are added.
   - It uses the **MappingLLM** AI model to map buggy code to its correct version.

4. **ReportResolver**:
   - Responsible for processing bug reports. It integrates multiple AI models in a sequence to resolve the reports. The models used include:
     - **FinderLLM**: Identifies which code file corresponds to a bug report.
     - **DebuggerLLM**: Automatically debugs the buggy code based on the bug report.
     - **TesterLLM**: Evaluates whether the debugged code functions correctly by comparing it with the correct code.

5. **Models**:
   - **MappingLLM**: Uses machine learning to generate code mappings from buggy code to correct code.
   - **FinderLLM**: Helps identify the file corresponding to the bug report.
   - **DebuggerLLM**: Uses AI to debug the code based on the provided bug report.
   - **TesterLLM**: Validates the correctness of the debugged code by comparing it with the expected correct code.

6. **Data Storage**:
   - The system stores mappings and resolved reports in JSON files:
     - `CodeMappings.json`: Stores mappings between buggy code and correct code.
     - `ResolvedReports.json`: Stores the status of bug reports after they have been processed.

## Components

### EmailServer and SlackServer

These components run as separate threads and listen for bug reports via email and Slack. Upon receiving a report, they store it in an internal queue for processing.

#### Key Features:
- **Socket Communication**: Both servers use socket programming to listen for incoming connections and receive bug report data.
- **Threading**: Both servers run as background threads, allowing the system to handle multiple bug reports concurrently.

### BugReportServer

The **BugReportServer** is responsible for handling incoming bug reports, whether they come from email or Slack. It processes the reports, storing them in separate queues for email and Slack reports, and ensures they are passed to the **ReportResolver** for further processing.

### CodeMappingManager

This component is responsible for managing code mappings between buggy code and correct code. It checks if there are any unmapped files, updates mappings for new files, and stores them in a JSON file for future use.

#### Key Features:
- **File Checking**: The system scans the buggy code directory and the correct code directory to check for files that haven’t been mapped yet.
- **Mapping Generation**: Uses the **MappingLLM** model to generate code mappings for unmapped files.

### ReportResolver

The **ReportResolver** processes incoming bug reports and resolves them by:
- Identifying the corresponding buggy code file using the **FinderLLM** model.
- Debugging the code using the **DebuggerLLM** model.
- Testing the debugged code using the **TesterLLM** model to ensure the fix works.

It periodically fetches bug reports from the queues and processes them in a loop.

#### Workflow:
1. **Bug Report Processing**:
   - The **FinderLLM** model identifies which buggy code file corresponds to a specific bug report.
   - The **DebuggerLLM** model debugs the identified code.
   - The **TesterLLM** model evaluates whether the debugged code solves the problem.

2. **Testing**:
   - If the initial fix doesn't work, the system retries the debugging process a few times, ensuring the best fix is found.
   
3. **Saving Results**:
   - Once a bug report is processed, it’s marked as either resolved or unresolved, and the details are saved in the `ResolvedReports.json` file.

### Models

The core of the system consists of four AI models that perform key tasks in the pipeline:

- **MappingLLM**: A model used to generate code mappings from buggy code to the correct code.
- **FinderLLM**: A model that finds which buggy code file corresponds to a bug report.
- **DebuggerLLM**: A model that debugs the code based on a bug report.
- **TesterLLM**: A model that evaluates whether the debugged code is correct.

Each model is used to process the bug reports, debug the code, and validate the changes.

## Installation

### Requirements

Before running this project, ensure that you have the following installed:

- **Python 3.x** (preferably Python 3.7 or higher)
- **Required Python Libraries**:
  - `openai` for interacting with GPT-based models
  - `python-dotenv` for managing environment variables
  - `socket` for creating the communication between servers
  - `subprocess` for running external scripts
  - `threading` for concurrent execution
  - `json` for storing mappings and reports

Install the dependencies using pip:

```bash
pip install -r requirements.txt