from textblob import TextBlob

# Welcome message
print("🐍 Welcome to Sentiment Spy! 🐍")

user_name = input("Please enter your name: ").strip()

# Default name if nothing is entered
if user_name == "":
    user_name = "Mystery Agent"

# List to store conversation history
# (Sentence, Polarity, Sentiment)
conversation_history = []

print(f"\nHello, Agent {user_name}!")
print("Type a sentence and I will analyze its sentiment.")
print("Commands: reset | history | exit\n")

while True:
    user_input = input(">> ").strip()

    # Check for empty input
    if user_input == "":
        print("Please enter a sentence or a valid command.")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"\nExiting Sentiment Spy. Goodbye, Agent {user_name}! 😊")
        break

    # Reset history
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print("Conversation history has been cleared.")
        continue

    # Display history
    elif user_input.lower() == "history":
        if len(conversation_history) == 0:
            print("No conversation history available.")
        else:
            print("\nConversation History")
            print("-" * 50)

            for index, (text, polarity, sentiment) in enumerate(conversation_history, start=1):

                if sentiment == "Positive":
                    emoji = "😊"
                elif sentiment == "Negative":
                    emoji = "😞"
                else:
                    emoji = "😐"

                print(f"{index}. {emoji} {text}")
                print(f"   Polarity : {polarity:.2f}")
                print(f"   Sentiment: {sentiment}\n")

        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        emoji = "😊"

    elif polarity < -0.25:
        sentiment = "Negative"
        emoji = "😞"

    else:
        sentiment = "Neutral"
        emoji = "😐"

    # Save to history
    conversation_history.append((user_input, polarity, sentiment))

    # Display result
    print(f"{emoji} {sentiment} Sentiment Detected!")
    print(f"Polarity Score: {polarity:.2f}\n")