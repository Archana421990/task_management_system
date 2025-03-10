import os
import sqlite3
import datetime
import csv

# Database Setup
DB_FILE = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending',
            due_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, due_date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    for task in tasks:
        print(task)

def update_task(task_id, status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def export_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Description", "Status", "Due Date"])
        writer.writerows(tasks)
    print("Tasks exported to tasks.csv")

def menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Export Tasks")
        print("6. Exit")
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
            update_task(task_id, status)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == "5":
            export_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    init_db()
    menu()
