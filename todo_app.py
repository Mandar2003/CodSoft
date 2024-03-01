import os

def display_menu():
    print("Welcome to To-Do List App")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    else:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def mark_task_done(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as done: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
