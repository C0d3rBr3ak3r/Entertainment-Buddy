import requests
from datetime import datetime
from APIs import TMDB_API_KEY,GOOGLE_BOOKS_API_KEY

# API Configuration
TMDB_API_KEY = TMDB_API_KEY
GOOGLE_BOOKS_API_KEY = GOOGLE_BOOKS_API_KEY
import requests

# Function to fetch upcoming movies
def get_upcoming_movies():
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("results", [])[:5]  # Get top 5 results
        return [{"title": movie["title"], "release_date": movie["release_date"]} for movie in movies]
    else:
        print("Failed to fetch upcoming movies.")
        return []

# Function to fetch upcoming TV shows
def get_upcoming_tv_shows():
    url = f"https://api.themoviedb.org/3/tv/on_the_air?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        tv_shows = response.json().get("results", [])[:5]  # Get top 5 results
        return [{"name": show["name"], "first_air_date": show["first_air_date"]} for show in tv_shows]
    else:
        print("Failed to fetch upcoming TV shows.")
        return []

# Function to fetch upcoming books (based on Google Books API)
def get_upcoming_books():
    query = "new releases"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&orderBy=newest&maxResults=5&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get("items", [])
        return [{"title": book["volumeInfo"]["title"], "published_date": book["volumeInfo"].get("publishedDate", "Unknown")} for book in books]
    else:
        print("Failed to fetch upcoming books.")
        return []

# Main Function
def display_upcoming_releases():
    print("Upcoming Movies:")
    for movie in get_upcoming_movies():
        print(f"- {movie['title']} (Release Date: {movie['release_date']})")
    
    print("\nUpcoming TV Shows:")
    for show in get_upcoming_tv_shows():
        print(f"- {show['name']} (First Air Date: {show['first_air_date']})")
    
    print("\nUpcoming Books:")
    for book in get_upcoming_books():
        print(f"- {book['title']} (Published Date: {book['published_date']})")

