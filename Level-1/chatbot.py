print("🤖 Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! Nice to meet you 😊")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is SimpleBot.")

    elif user_input == "what can you do":
        print("Bot: I can chat with you using simple rules.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
