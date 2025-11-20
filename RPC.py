import random

print("🎮 Welcome to Rock Paper Scissors!")

# Choices
options = ["rock", "paper", "scissors"]
emojis = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

while True:
    user = input("\n👉 Enter rock/paper/scissors or 'q' to quit: ").lower()

    if user == "q":
        print("👋 Thanks for playing!")
        break

    if user not in options:
        print("⚠️ Invalid choice! Try again.")
        continue

    computer = random.choice(options)

    print(f"\n🧍 You chose: {user} {emojis[user]}")
    print(f"🤖 Computer chose: {computer} {emojis[computer]}")

    # Game logic
    if user == computer:
        print("😮 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("💀 You lose!")
