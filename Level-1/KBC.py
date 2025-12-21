print("\n🎉 Welcome to Kaun Banega Crorepati! 🎉")

questions = [
    {
        "question": "Which is the national animal of India?",
        "options": ["A) Tiger", "B) Lion", "C) Elephant", "D) Panther"],
        "answer": "A"
    },
    {
        "question": "Who is known as the Father of the Indian Constitution?",
        "options": ["A) Mahatma Gandhi", "B) B. R. Ambedkar", "C) Nehru", "D) Sardar Patel"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    }
]

prize = ["₹10,000", "₹50,000", "₹1,00,000"]

for i, q in enumerate(questions):
    print(f"\n🟦 Question {i+1} for {prize[i]}")
    print(q["question"])

    for opt in q["options"]:
        print(opt)

    while True:
        ans = input("👉 Your answer (A/B/C/D or Q to quit): ").upper()

        if ans == "Q":
            print("\nYou quit the game.")
            if i == 0:
                print("💰 You won: ₹0")
            else:
                print(f"💰 You won: {prize[i-1]}")
            exit()

        if ans in ["A", "B", "C", "D"]:
            if ans == q["answer"]:
                print("✔ Correct! 🎉")
                print(f"💰 You won {prize[i]}")
                break
            else:
                print("❌ Wrong answer!")
                print("Game Over!")
                if i == 0:
                    print("💰 You won: ₹0")
                else:
                    print(f"💰 You won: {prize[i-1]}")
                exit()
        else:
            print("Invalid input, try again.")

print("\n🏆 You won ₹1,00,000! Congratulations! 🎉")
