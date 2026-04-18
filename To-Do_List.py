tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        priority = input("Enter priority (High/Medium/Low): ")
        tasks.append((task, priority))
        print("Task added!")

    elif choice == 2:
        print("\n--- Task List ---")
        for t, p in tasks:
            print(f"{t} [{p}]")

    elif choice == 3:
        break

    else:
        print("Invalid choice")