def display_menu():
    print("\nTo-Do List Application")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task added successfully.")

def delete_task(tasks):
    view_task(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been deleted successfully.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def to_do_list():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter Your Choice (1-4): ")
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, Please try again.")

to_do_list()