print("🧠 Welcome to the Quiz Game")

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Chennai", "D) Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) Java", "C) HTML", "D) C"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A) Dennis Ritchie", "B) Guido van Rossum", "C) James Gosling", "D) Bjarne Stroustrup"],
        "answer": "B"
    }
]

score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1)
    print(questions[i]["question"])

    for opt in questions[i]["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == questions[i]["answer"]:
        print("✔ Correct")
        score += 1
    else:
        print("❌ Wrong")

print("\n🎯 Quiz Finished")
print("Your Score:", score, "/", len(questions))
