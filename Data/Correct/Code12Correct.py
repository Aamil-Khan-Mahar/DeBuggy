# Correct Code
# filename: Code12Correct.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        return f"Task '{task}' added."

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task and not t["completed"]:
                t["completed"] = True
                return f"Task '{task}' marked as completed."
        return f"Task '{task}' not found or already completed."

    def show_tasks(self):
        if not self.tasks:
            return "No tasks in the list."
        return "\n".join([f"[{'X' if t['completed'] else ' '}] {t['task']}" for t in self.tasks])
