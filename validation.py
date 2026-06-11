from datetime import datetime


def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Invalid title")
    return True


def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Invalid description")
    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date")
    return True