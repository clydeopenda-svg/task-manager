from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Invalid task details. Please try again.")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending):
            print(f"{i + 1}. {task['title']} - {task['description']} (Due: {task['due_date']})")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = len([task for task in tasks if task["completed"]])
        progress = (completed / len(tasks)) * 100
    return progress