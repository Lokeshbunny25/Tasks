def chatbot():

    print("===== Simple Chatbot =====")
    print("Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


                                                                                                                                        
chatbot()