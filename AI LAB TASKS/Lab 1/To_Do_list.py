
tasks = ["Shopping ","Gardening","coding"]

def show_menu():
    print("\n-- To-Do List Menu --")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(i+1,":",tasks[i])
def add_task():
    task = input("\nEnter a task to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")
def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting the To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
