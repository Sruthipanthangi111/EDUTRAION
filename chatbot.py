def chatbot():
    print("Hi! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("Bot: Hello! How can I help you?")
        elif "your name" in user_input:
            print("Bot: I am RuleBot, your virtual assistant.")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing fine!")
        elif "help" in user_input:
            print("Bot: Sure, I can help. What do you need help with?")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()