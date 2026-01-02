FILE = "faves.txt"

def load_faves():
    try:
        with open(FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_faves(faves):
    with open(FILE, "w") as f:
        for item in faves:
            f.write(item + "\n")

faves = load_faves()

while True:
    print("\n💖 Faves List")
    print("1. Add Favorite")
    print("2. View Favorites")
    print("3. Remove Favorite")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Enter favorite item: ")
        faves.append(item)
        save_faves(faves)
        print("✅ Added to favorites")

    elif choice == "2":
        if not faves:
            print("No favorites yet")
        else:
            for i, item in enumerate(faves, 1):
                print(i, item)

    elif choice == "3":
        num = int(input("Enter number to remove: "))
        if 1 <= num <= len(faves):
            faves.pop(num - 1)
            save_faves(faves)
            print("❌ Removed")
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
