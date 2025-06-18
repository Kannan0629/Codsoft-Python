# To-Do List stored as a list of dictionaries
todo_list = []

def add_task():
    task = input("Enter the task description: ")
    todo_list.append({"task": task, "completed": False})
    print("✅ Task added successfully.\n")

def view_tasks():
    if not todo_list:
        print("📭 No tasks found.\n")
        return
    print("\n📝 To-Do List:")
    for i, item in enumerate(todo_list, 1):
        status = "✅ Done" if item['completed'] else "❌ Pending"
        print(f"{i}. {item['task']} - {status}")
    print()

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("🎉 Task marked as completed.\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_desc = input("Enter the new task description: ")
            todo_list[task_num - 1]['task'] = new_desc
            print("✏️ Task updated successfully.\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
            print("🗑️ Task deleted successfully.\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

def todo_menu():
    while True:
        print("📋 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.\n")

# Run the application
todo_menu()
1