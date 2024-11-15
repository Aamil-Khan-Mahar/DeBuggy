import unittest
from Code12Correct.py import ToDoList  

class TestToDoList(unittest.TestCase):

    def setUp(self):
        """Set up a fresh ToDoList instance before each test."""
        self.todo = ToDoList()

    def test_add_task(self):
        # Test adding a task to the list
        task = "Buy groceries"
        result = self.todo.add_task(task)
        self.assertEqual(result, f"Task '{task}' added.")
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["task"], task)
        self.assertFalse(self.todo.tasks[0]["completed"])

    def test_complete_task(self):
        # Test completing a task
        task = "Buy groceries"
        self.todo.add_task(task)
        result = self.todo.complete_task(task)
        self.assertEqual(result, f"Task '{task}' marked as completed.")
        self.assertTrue(self.todo.tasks[0]["completed"])

    def test_complete_task_not_found(self):
        # Test attempting to complete a task that doesn't exist
        task = "Buy groceries"
        result = self.todo.complete_task(task)
        self.assertEqual(result, f"Task '{task}' not found or already completed.")

    def test_complete_task_already_completed(self):
        # Test completing a task that is already marked as completed
        task = "Buy groceries"
        self.todo.add_task(task)
        self.todo.complete_task(task)
        result = self.todo.complete_task(task)
        self.assertEqual(result, f"Task '{task}' not found or already completed.")

    def test_show_tasks_empty(self):
        # Test showing tasks when the list is empty
        result = self.todo.show_tasks()
        self.assertEqual(result, "No tasks in the list.")

    def test_show_tasks(self):
        # Test showing tasks when there are tasks in the list
        self.todo.add_task("Buy groceries")
        self.todo.add_task("Clean the house")
        result = self.todo.show_tasks()
        expected = "[ ] Buy groceries\n[ ] Clean the house"
        self.assertEqual(result, expected)

    def test_show_tasks_with_completed(self):
        # Test showing tasks with some completed
        self.todo.add_task("Buy groceries")
        self.todo.add_task("Clean the house")
        self.todo.complete_task("Buy groceries")
        result = self.todo.show_tasks()
        expected = "[X] Buy groceries\n[ ] Clean the house"
        self.assertEqual(result, expected)

    def test_add_multiple_tasks(self):
        # Test adding multiple tasks
        self.todo.add_task("Buy groceries")
        self.todo.add_task("Clean the house")
        self.todo.add_task("Finish homework")
        result = self.todo.show_tasks()
        expected = "[ ] Buy groceries\n[ ] Clean the house\n[ ] Finish homework"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

