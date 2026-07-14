import re
import random

# Destinations based on category
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

# List of travel jokes
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to clean user input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


# Function to recommend a destination
def recommend():
    print("\nTravelBot: What do you prefer?")
    print("Options: beaches, mountains, cities")

    preference = normalize_input(input("You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(f"\nTravelBot: How about visiting {suggestion}?")
        answer = normalize_input(input("Do you like this suggestion? (yes/no): "))

        if answer == "yes":
            print(f"TravelBot: Great! Have an amazing trip to {suggestion}. 😊")

        elif answer == "no":
            print("TravelBot: No worries! Let me suggest another place.\n")
            recommend()

        else:
            print("TravelBot: I didn't understand. Let's try again.\n")
            recommend()

    else:
        print("TravelBot: Sorry, I don't have recommendations for that category.\n")
        recommend()


# Function to give packing tips
def packing_tips():
    location = normalize_input(input("\nTravelBot: Where are you going? "))
    days = input("TravelBot: How many days is your trip? ")

    print(f"\nPacking Tips for {days} days in {location.title()}:")
    print("- Pack comfortable and versatile clothes.")
    print("- Carry chargers and power adapters.")
    print("- Check the weather before leaving.")
    print("- Keep important documents with you.")
    print("- Carry a water bottle and basic medicines.\n")


# Function to tell a random joke
def tell_joke():
    print("\nTravelBot:")
    print(random.choice(jokes))
    print()


# Function to display available commands
def show_help():
    print("\n========== TravelBot Help ==========")
    print("recommendation - Get a travel recommendation")
    print("packing        - Get packing tips")
    print("joke           - Hear a travel joke")
    print("help           - Show this menu")
    print("exit / bye     - End the chatbot")
    print("====================================\n")


# Main chatbot function
def chat():
    print("🌍 Welcome to TravelBot!")

    name = input("Please enter your name: ").strip()

    if name == "":
        name = "Traveler"

    print(f"\nHello, {name}! Nice to meet you.")

    show_help()

    while True:
        user_input = normalize_input(input(f"{name}: "))

        if "recommend" in user_input or "suggest" in user_input:
            recommend()

        elif "pack" in user_input or "packing" in user_input:
            packing_tips()

        elif "joke" in user_input or "funny" in user_input:
            tell_joke()

        elif "help" in user_input:
            show_help()

        elif "exit" in user_input or "bye" in user_input:
            print("\nTravelBot: Safe travels! Goodbye. 👋")
            break

        else:
            print("TravelBot: Sorry, I didn't understand that.")
            print("Type 'help' to see what I can do.\n")


# Start the chatbot
if __name__ == "__main__":
    chat()