
import tkinter as tk
from PIL import Image, ImageTk
import requests

# Function to retrieve movie data from the TMDb API based on the movie name
def fetch_movie_data(movie_name):
    api_key = '8213f0ca3c6e2b3c647512b7ccc10f64'
    api_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"

    try:
        response = requests.get(api_url)
        response_data = response.json()

        if response_data.get('results'):
            # The API returned movie data successfully
            movie_data = response_data['results']
            return movie_data
        else:
            # The movie was not found or there was an error
            print("Error accessing the TMDb API.")
            return None

    except requests.exceptions.RequestException as e:
        print("Error accessing the TMDb API:", e)
        return None

# Function to analyze sentiment of movie reviews from the TMDb API
def sentiment_analyzer_from_api():
    global review_entry

    # Get the movie name entered by the user
    movie_name = review_entry.get()

    if movie_name:
        # Fetch movie data from the TMDb API
        movie_data = fetch_movie_data(movie_name)

        if movie_data:
            # Assuming that movie_data contains a list of dictionaries with movie details,
            # you can perform sentiment analysis on the reviews, for example:
            ratings = [movie['vote_average'] for movie in movie_data]
            average_sentiment = sum(ratings) / len(ratings)

            if average_sentiment == 0:
                display_emoji(0x1F610, "Neutral")
            elif average_sentiment < 5:
                display_emoji(0x1F62B, "Negative")
            elif average_sentiment >= 7:
                display_emoji(0x1F604, "Positive")
            else:
                display_emoji(0x1F642, "Mixed")
        else:
            sentiment_label.config(text="Movie not found.", font=("Arial", 16))

# ... (Rest of the code for GUI setup, widgets, and main loop)

# (The remaining code is the same as your original code)


# ... (Rest of the code for GUI setup, widgets, and main loop)

def display_emoji(unicode_code, sentiment_text):
    emoji = chr(unicode_code)
    sentiment_label.config(text=sentiment_text + " " + emoji, font=("Arial", 16))

app = tk.Tk()
app.title("Sentiment Analysis by BESURAS UNITED")
app.geometry("800x600")  # Adjust the window size as needed

def create_header():
    header_frame = tk.Frame(app)
    header_frame.grid(row=0, column=0, sticky="n")

    title_label = tk.Label(header_frame, text="BESURAS UNITED", font=("Arial", 24, "bold"))
    title_label.grid(row=0, column=0, padx=10, pady=10)

    nav_frame = tk.Frame(header_frame)
    nav_frame.grid(row=1, column=0, padx=10, pady=10)



def create_content():
    content_frame = tk.Frame(app)
    content_frame.grid(row=20, column=0, sticky="s",padx=330,pady=50)

    welcome_label = tk.Label(content_frame, text="Welcome to Movie Review Sentiment Analysis using NLP by BESURAS UNITED", font=("Arial", 20, "bold"))
    welcome_label.pack(pady=10)

    introduction_label = tk.Label(content_frame, text="INTRODUCTION", font=("Arial", 16, "bold"))
    introduction_label.pack(pady=5)

    introduction_text = """
    Data is being produced at an astounding rate and volume in the field of the internet and other digital
    services nowadays. Researchers, engineers, and data analysts often work with tabular or statistical data.
    There may be categorical or numerical data in each of these tabular data columns. Various data formats,
    including text, picture, video, and audio, are present in data that is generated. Analysis of unstructured
    data is produced by online behaviour such as publications, web content, blog entries, and social media
    platforms. To effectively build their business, corporations and businesses ONE must examine textual
    data to comprehend consumer behaviours, opinions, and comments. Text analytics is developing at a
    higher pace in order to deal with massive text information.
    """
    introduction_paragraph = tk.Label(content_frame, text=introduction_text, font=("Arial", 12))
    introduction_paragraph.pack(pady=5)


background_image = Image.open("images/hh.jpg")
background_image = background_image.resize((1550, 1000))  # Match the window size
my = ImageTk.PhotoImage(background_image)

label = tk.Label(image=my)
label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the background image at (0, 0) with full window size

# Center the review_entry and analyse_button in the middle of the page using grid
review_entry = tk.Entry(app, width=50)
review_entry.grid(row=0, column=0, padx=10, pady=(350, 0), ipady=5)

# Center the analyse_button near the review_entry using grid
analyse_button = tk.Button(app, text="Analyse", command=sentiment_analyzer_from_api, fg="black", bg="sky blue")
analyse_button.grid(row=1, column=0, padx=0, pady=(10, 0))

# Create an empty frame to add vertical space at the bottom of the window
empty_frame = tk.Frame(app, height=1)
empty_frame.grid(row=2, column=0, columnspan=5)

sentiment_label = tk.Label(app, text="", font=("Arial", 16))
sentiment_label.grid(row=3, column=0, columnspan=2, pady=10)



create_header()
create_content()
app.mainloop()
