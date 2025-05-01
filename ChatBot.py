def chatbot():
    print("🤖 Hello! Welcome to ShopEasy Customer Support.")
    print("How can I assist you today? (type 'exit' to quit)")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['exit', 'quit', 'bye']:
            print("🤖 Thank you for contacting ShopEasy. Have a great day!")
            break

        elif "hours" in user_input or "time" in user_input:
            print("🤖 Our support is available 24/7!")

        elif "return" in user_input or "refund" in user_input:
            print("🤖 You can return any item within 30 days of purchase. Refunds are processed within 5-7 business days.")

        elif "order status" in user_input or "where is my order" in user_input:
            print("🤖 You can track your order by logging into your account and checking 'My Orders'.")

        elif "payment" in user_input:
            print("🤖 We accept Credit/Debit cards, UPI, Net Banking, and Cash on Delivery.")

        elif "contact" in user_input or "email" in user_input:
            print("🤖 You can reach us at support@shopeasy.com or call us at 1800-123-456.")

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Hello there! How can I help you today?")

        else:
            print("🤖 I'm sorry, I didn't understand that. Could you please rephrase or ask something else?")

# Run the chatbot
chatbot()

#Output
#🤖 Hello! Welcome to ShopEasy Customer Support.
#How can I assist you today? (type 'exit' to quit)
#You: what are your working hours?
#🤖 Our support is available 24/7!
#You: how do I return an item?
#🤖 You can return any item within 30 days of purchase. Refunds are processed within 5-7 business days.
#You: bye
#🤖 Thank you for contacting ShopEasy. Have a great day!
