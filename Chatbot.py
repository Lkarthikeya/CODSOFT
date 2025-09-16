
def chatbot_response(user_input):
    """
    Function to generate chatbot responses based on simple rules.
    """

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you today?"
    

    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! 😄 How about you?"
    

    elif "your name" in user_input:
        return "I’m a simple chatbot 🤖 created using Python and rule-based logic."
    

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! 👋 Have a wonderful day!"
    

    elif "weather" in user_input:
        return "I can’t check the weather 🌦️ right now, but you can ask a weather app!"
    

    else:
        return "Hmm 🤔 I don’t understand that yet. Could you try rephrasing?"


print("🤖 Chatbot: Hi! I'm your chatbot. Type 'bye' anytime to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)


    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
