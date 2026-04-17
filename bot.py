print("Bot: Hello, I am a simple ChatBot. Type 'Quit' to exit.")

while True:
    user_input = input("You: ").lower()
    if "quit" in user_input or "exit" in user_input:
        print("Bot: Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello there! How can I help you today?")
    elif "name" in user_input:
        print("Bot: I am PyBot, a simple rule-based chatbot")
    elif "how are you?" in user_input:
        print("I'm just code, but I'm running perfectly!")
    elif "weather" in user_input:
        print("Bot: I don't know the weather. I am very simple")
    elif "help" in user_input:
        print("Bot: You can ask me about my name, how i am, or just say hello")
    else:
        print("Bot: I don't understand that. Try saying 'hello' or 'help'.")
        