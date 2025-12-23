print("🌲 Welcome to the Adventure Game 🌲")
print("You are standing at the entrance of a dark forest.")

choice1 = input("Do you want to go LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("\nYou walk towards a river.")
    choice2 = input("Do you want to SWIM or CROSS the bridge? ").lower()

    if choice2 == "swim":
        print("\n🐊 Oh no! A crocodile attacked you.")
        print("❌ Game Over")

    elif choice2 == "cross":
        print("\n🏆 You safely crossed the river and found a treasure!")
        print("🎉 You Win!")

    else:
        print("❗ Invalid choice. Game Over.")

elif choice1 == "right":
    print("\nYou enter a dark cave.")
    choice2 = input("Do you want to ENTER deeper or RUN away? ").lower()

    if choice2 == "enter":
        print("\n🧙 A wizard gives you gold for your bravery!")
        print("🎉 You Win!")

    elif choice2 == "run":
        print("\n😨 You ran away safely but found nothing.")
        print("Game Ended.")

    else:
        print("❗ Invalid choice. Game Over.")

else:
    print("❗ Invalid direction. Game Over.")
