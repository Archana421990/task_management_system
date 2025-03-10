import sqlite3
from datetime import datetime

# Database setup
def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT CHECK(status IN ('Pending', 'Completed')) DEFAULT 'Pending',
                        due_date TEXT)''')
    conn.commit()
    conn.close()

# Function to add a task
def add_task(title, description, due_date):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
                   (title, description, due_date))
    conn.commit()
    conn.close()
    print("Task added successfully!")

# Function to list all tasks
def view_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}, Due Date: {task[4]}")

# Function to update a task's status
def update_task_status(task_id, status):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()
    print("Task updated successfully!")

# Function to delete a task
def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully!")

# Command-line menu
def menu():
    init_db()
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (Pending/Completed): ")
            update_task_status(task_id, status)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
