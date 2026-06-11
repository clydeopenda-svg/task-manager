from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):

    if not validate_task_title(title):
        raise ValueError("Invalid title")

    if not validate_task_description(description):
        raise ValueError("Invalid description")

    if not validate_due_date(due_date):
        raise ValueError("Invalid due date")

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        raise ValueError("Invalid task index")


def view_pending_tasks(tasks=tasks):

    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    for task in pending_tasks:
        print(task)

    return pending_tasks


def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100

    return progress
