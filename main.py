from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)


def main():

    while True:

        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input()
            desc = input()
            due = input()
            add_task(title, desc, due)

        elif choice == "2":
            index = input()
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            print(calculate_progress())

        elif choice == "5":
            break


if __name__ == "__main__":
    main()