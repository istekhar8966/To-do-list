# all the tasks will be stored here
tasks = []

 # Main lopp start's from here
while True:
    print("\n--- To-Do List ---")
    print("\n1. Add task(+)")
    print("2. View all tasks")
    print("3. Delete all tasks")
    print("4. Exit")
    choice = input("\n Select one(1-4): ")
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks yet")
        else:
            print("\nYour Tasks!")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}") 
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting... Bye!")
        break
    
    else:
        print("Invalid choice! Try again. ")
