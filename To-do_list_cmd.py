# Create an empty list to store tasks
tasks = []

# Function to create a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

# Function to view tasks
def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to update tasks
def edit_task():
    show_tasks()
    try:
        task_index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index] = input("Change task : ")
            print("Task Changed!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter the task index.")

# Function to remove a task
def remove_task():
    show_tasks()
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter the task number as a number.")

# Main loop for the to-do list
while True:
    print("\nOptions:")
    print("1. Create a task")
    print("2. View tasks")
    print("3. Update tasks")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
    
