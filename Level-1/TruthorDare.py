import random

truths = [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What is your secret talent?",
    "Who is your crush?",
    "What is the most embarrassing moment of your life?"
]

dares = [
    "Do 10 jumping jacks.",
    "Sing a song loudly.",
    "Talk like a robot for 30 seconds.",
    "Do 5 push-ups.",
    "Clap your hands for 20 seconds."
]

print("🎉 Welcome to Truth or Dare 🎉")

while True:
    choice = input("\nChoose Truth or Dare (T/D) or Q to quit: ").upper()

    if choice == "T":
        print("\n🧠 TRUTH:")
        print(random.choice(truths))

    elif choice == "D":
        print("\n🔥 DARE:")
        print(random.choice(dares))

    elif choice == "Q":
        print("\n👋 Thanks for playing!")
        break

    else:
        print("❗ Invalid choice. Please enter T, D, or Q.")
