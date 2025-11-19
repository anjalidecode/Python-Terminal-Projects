import random

print("🎲 Welcome to the Dice Rolling Simulator! 🎲")

while True:
    user = input("\n👉 Press ENTER to roll the dice or type 'q' to quit: ")

    if user.lower() == 'q':
        print("👋 Thanks for playing!")
        break

    # Generate a random number between 1 and 6
    roll = random.randint(1, 6)

    print(f"\n🎯 You rolled: {roll} ")
