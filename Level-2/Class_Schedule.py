import json
import os

FILE = "schedule.json"

# Load schedule
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        schedule = json.load(f)
else:
    schedule = []

def save_schedule():
    with open(FILE, "w") as f:
        json.dump(schedule, f)

while True:
    print("\n📝 Class Schedule")
    print("1. Add Class")
    print("2. View Schedule")
    print("3. Delete Class")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        day = input("Enter day: ")
        subject = input("Enter subject: ")
        time = input("Enter time: ")

        schedule.append({
            "day": day,
            "subject": subject,
            "time": time
        })

        save_schedule()
        print("✅ Class added")

    elif choice == "2":
        if not schedule:
            print("No classes scheduled")
        else:
            for i, cls in enumerate(schedule, 1):
                print(f"{i}. {cls['day']} - {cls['subject']} at {cls['time']}")

    elif choice == "3":
        num = int(input("Enter class number to delete: "))
        if 1 <= num <= len(schedule):
            schedule.pop(num - 1)
            save_schedule()
            print("❌ Class removed")
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
