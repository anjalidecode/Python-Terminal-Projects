import random

# List of fortune messages
fortunes = [
    "🌞 You will have a great day!",
    "🎁 A surprise is waiting for you.",
    "💪 Believe in yourself and success will follow.",
    "📩 Good news will come to you soon.",
    "🏆 Your hard work will pay off.",
    "🌍 Adventure is on your horizon.",
    "🤝 You will meet someone helpful today.",
    "🔍 Something you lost will soon turn up.",
    "😊 A pleasant experience is coming your way.",
    "🧠 Trust your instincts—they are right!"
]

# Select a random message
fortune = random.choice(fortunes)

# Display the fortune
print("🥠 Your Fortune Cookie says:")
print(f"{fortune}")