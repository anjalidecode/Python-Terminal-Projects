FILE = "todo.txt"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n📋 To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added")

    elif choice == "2":
        if not tasks:
            print("No tasks found")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, t)

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("❌ Task deleted")
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
