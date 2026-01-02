FILE = "grocery.txt"

def load_items():
    try:
        with open(FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_items(items):
    with open(FILE, "w") as f:
        for item in items:
            f.write(item + "\n")

items = load_items()

while True:
    print("\n🛒 Grocery List")
    print("1. Add Item")
    print("2. View Items")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Enter grocery item: ")
        items.append(item)
        save_items(items)
        print("✅ Item added")

    elif choice == "2":
        if not items:
            print("Grocery list is empty")
        else:
            for i, item in enumerate(items, 1):
                print(i, item)

    elif choice == "3":
        num = int(input("Enter item number to remove: "))
        if 1 <= num <= len(items):
            items.pop(num - 1)
            save_items(items)
            print("❌ Item removed")
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
