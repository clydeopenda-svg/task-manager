from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):

    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):

    try:
        index = int(index)
    except ValueError:
        return

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):

    pending = [t for t in tasks if not t["completed"]]

    for task in pending:
        print(task)

    return pending


def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        print("0.00%")
        return 0

    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100

    print(f"{progress:.2f}%")
    return progress