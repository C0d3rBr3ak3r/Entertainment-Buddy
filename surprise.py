import random
import requests
from APIs import TMDB_API_KEY,GOOGLE_BOOKS_API_KEY

TMDB_API_KEY = TMDB_API_KEY
GOOGLE_BOOKS_API_KEY = GOOGLE_BOOKS_API_KEY


def fetch_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        return [{"type": "Movie", "title": movie["title"], "description": movie.get("overview", "No description available")}
                for movie in movies]
    return []

# Function to fetch TV shows
def fetch_tv_shows():
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        tv_shows = response.json().get("results", [])
        return [{"type": "TV Show", "title": show["name"], "description": show.get("overview", "No description available")}
                for show in tv_shows]
    return []

# Function to fetch books
def fetch_books():
    url = f"https://www.googleapis.com/books/v1/volumes?q=best%20books&maxResults=10&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get("items", [])
        return [{"type": "Book", "title": book["volumeInfo"]["title"], "description": book["volumeInfo"].get("description", "No description available")}
                for book in books]
    return []

# Surprise Me Functionality
def surprise_me():
    # Fetch all categories
    movies = fetch_movies()
    tv_shows = fetch_tv_shows()
    books = fetch_books()
    
    # Combine all recommendations
    combined_recommendations = movies + tv_shows + books
    
    if not combined_recommendations:
        return "No recommendations available at the moment. Please try again later."
    
    # Randomly select one recommendation
    surprise_pick = random.choice(combined_recommendations)
    return f"Surprise! Here's something you might like:\n\nType: {surprise_pick['type']}\nTitle: {surprise_pick['title']}\nDescription: {surprise_pick['description']}"
