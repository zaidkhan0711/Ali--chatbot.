import nltk

nltk.download('punkt')

print("Ali Chatbot")
print("Type 'exit' to quit.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Ali: Goodbye!")
        break
    elif "hello" in user.lower() or "hi" in user.lower():
        print("Ali: Hello! How can I help you?")
    elif "how are you" in user.lower():
        print("Ali: I am fine. Thanks!")
    else:
        print("Ali: Sorry, I don't understand.")
