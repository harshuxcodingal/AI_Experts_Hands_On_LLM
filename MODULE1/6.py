import time
import pandas as pd
from textblob import TextBlob

# Load the dataset
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print("Error: 'imdb_top_1000.csv' was not found.")
    exit()

# Get all unique genres
genres = sorted({
    genre.strip()
    for genre_list in df["Genre"].dropna().str.split(", ")
    for genre in genre_list
})


# Loading animation
def dots():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()


# Convert polarity into sentiment
def sentiment_label(polarity):
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"


# Recommend movies
def recommend(genre=None, mood=None, rating=None, n=5):

    filtered_df = df

    # Filter by genre
    if genre:
        filtered_df = filtered_df[
            filtered_df["Genre"].str.contains(genre, case=False, na=False)
        ]

    # Filter by minimum rating
    if rating is not None:
        filtered_df = filtered_df[
            filtered_df["IMDB_Rating"] >= rating
        ]

    if filtered_df.empty:
        return "No suitable movie recommendations found."

    # Shuffle movies
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for _, row in filtered_df.iterrows():

        overview = row["Overview"]

        if pd.isna(overview):
            continue

        polarity = TextBlob(overview).sentiment.polarity

        if mood is None or polarity >= 0:
            recommendations.append(
                (row["Series_Title"], polarity)
            )

        if len(recommendations) == n:
            break

    if recommendations:
        return recommendations

    return "No suitable movie recommendations found."


# Display recommendations
def show_recommendations(recommendations, user_name):

    print(f"\n🎬 Movie Recommendations for {user_name}\n")

    for index, (title, polarity) in enumerate(recommendations, start=1):
        print(f"{index}. {title}")
        print(f"   Sentiment : {sentiment_label(polarity)}")
        print(f"   Polarity  : {polarity:.2f}\n")


# Select genre
def get_genre():

    print("Available Genres:\n")

    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")

    while True:

        choice = input("\nEnter genre number or name: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(genres):
                return genres[choice - 1]

        else:

            choice = choice.title()

            if choice in genres:
                return choice

        print("Invalid input. Please try again.")


# Select rating
def get_rating():

    while True:

        rating = input(
            "Enter minimum IMDB rating (7.6 - 9.3) or type 'skip': "
        ).strip()

        if rating.lower() == "skip":
            return None

        try:
            rating = float(rating)

            if 7.6 <= rating <= 9.3:
                return rating

            print("Rating should be between 7.6 and 9.3.")

        except ValueError:
            print("Please enter a valid number.")


# ---------------- MAIN PROGRAM ----------------

print("🎥 Welcome to the Movie Recommendation Assistant! 🎥\n")

user_name = input("Enter your name: ").strip()

if user_name == "":
    user_name = "Movie Lover"

print(f"\nHello, {user_name}! Let's find a movie for you.\n")

genre = get_genre()

mood = input("\nHow are you feeling today? ").strip()

print("\nAnalyzing your mood", end="")
dots()

mood_polarity = TextBlob(mood).sentiment.polarity

if mood_polarity > 0:
    mood_type = "Positive 😊"
elif mood_polarity < 0:
    mood_type = "Negative 😞"
else:
    mood_type = "Neutral 😐"

print(f"Your mood is {mood_type}")
print(f"Polarity Score: {mood_polarity:.2f}\n")

rating = get_rating()

print("\nFinding the best movies for you", end="")
dots()

recommendations = recommend(
    genre=genre,
    mood=mood,
    rating=rating,
    n=5
)

if isinstance(recommendations, str):
    print(recommendations)
else:
    show_recommendations(recommendations, user_name)


# Ask for more recommendations
while True:

    choice = input("\nWould you like more recommendations? (yes/no): ").lower()

    if choice == "yes":

        recommendations = recommend(
            genre=genre,
            mood=mood,
            rating=rating,
            n=5
        )

        if isinstance(recommendations, str):
            print(recommendations)
        else:
            show_recommendations(recommendations, user_name)

    elif choice == "no":
        print(f"\nEnjoy your movies, {user_name}! 🍿🎬")
        break

    else:
        print("Please enter 'yes' or 'no'.")