import csv

class Task:
    def __init__(self, task_id, title, description, status, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

def export_tasks_to_csv(tasks, filename="tasks.csv"):
    """Exports a list of tasks to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Description", "Status", "Due Date"])  # Header row
        for task in tasks:
            writer.writerow([task.task_id, task.title, task.description, task.status, task.due_date])

# Example tasks
tasks = [
    Task(1, "Buy groceries", "Milk, Eggs, Bread", "Pending", "2025-03-15"),
    Task(2, "Submit project", "Complete and submit task app", "Completed", "2025-03-10")
]

# Export tasks to CSV
export_tasks_to_csv(tasks)
print("Tasks exported successfully!")
