import sys
import os

def compare_classes():
    """
    Compares the ToDoList class functionality from both the correct and buggy code:
    - Checks if function names and logic match.
    - Tests if the functions return the expected results for adding, completing, and displaying tasks.
    Returns True if both match; False otherwise.
    """
    try:
        # Test both the correct and buggy versions of the ToDoList class
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct.Code12Correct import ToDoList as CorrectToDoList
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code12Buggy import ToDoList as BuggyToDoList
        sys.path.remove(buggy_path)

        # Test cases for correct functionality
        correct_todo = CorrectToDoList()
        buggy_todo = BuggyToDoList()

        # Add tasks
        correct_add = correct_todo.add_task("Buy groceries")
        buggy_add = buggy_todo.add_task("Buy groceries")

        # Complete tasks
        correct_complete = correct_todo.complete_task("Buy groceries")
        buggy_complete = buggy_todo.complete_task("Buy groceries")

        # Show tasks
        correct_show = correct_todo.show_tasks()
        buggy_show = buggy_todo.show_tasks()

        # Test results for each function
        if correct_add != buggy_add:
            print(f"Add task mismatch: Correct: {correct_add}, Buggy: {buggy_add}")
            return False
        if correct_complete != buggy_complete:
            print(f"Complete task mismatch: Correct: {correct_complete}, Buggy: {buggy_complete}")
            return False
        if correct_show != buggy_show:
            print(f"Show tasks mismatch: Correct: {correct_show}, Buggy: {buggy_show}")
            return False

        # Additional test for the buggy initialization (wrong class name in the buggy code)
        try:
            buggy_todo_invalid = BuggyToDoList()  # This should fail due to the typo in 'ToDoListt'
        except TypeError:
            print("Buggy code fails correctly due to incorrect class name 'ToDoListt'.")
            return False

        return True
    
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return False


# Run the comparison
if __name__ == "__main__":
    print(compare_classes())
