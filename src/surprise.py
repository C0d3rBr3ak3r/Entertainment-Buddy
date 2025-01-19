import random
import requests
from APIs import TMDB_API_KEY, GOOGLE_BOOKS_API_KEY

TMDB_API_KEY = TMDB_API_KEY
GOOGLE_BOOKS_API_KEY = GOOGLE_BOOKS_API_KEY


def fetch_movies():
    """
    Fetch popular movies from the TMDB API.

    Returns:
        list[dict]: A list of dictionaries, each containing the type, title, and description of a movie.
    """
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        return [{"type": "Movie", "title": movie["title"], "description": movie.get("overview", "No description available")}
                for movie in movies]
    return []


def fetch_tv_shows():
    """
    Fetch popular TV shows from the TMDB API.

    Returns:
        list[dict]: A list of dictionaries, each containing the type, title, and description of a TV show.
    """
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        tv_shows = response.json().get("results", [])
        return [{"type": "TV Show", "title": show["name"], "description": show.get("overview", "No description available")}
                for show in tv_shows]
    return []


def fetch_books():
    """
    Fetch popular books from the Google Books API.

    Returns:
        list[dict]: A list of dictionaries, each containing the type, title, and description of a book.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q=best%20books&maxResults=10&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get("items", [])
        return [{"type": "Book", "title": book["volumeInfo"]["title"], "description": book["volumeInfo"].get("description", "No description available")}
                for book in books]
    return []


def surprise_me():
    """
    Provide a random recommendation from movies, TV shows, or books.

    Fetches popular data from APIs and combines them into a single list, 
    then randomly selects one entry to present as a surprise recommendation.

    Returns:
        str: A formatted string with the type, title, and description of the recommendation.
    """
    movies = fetch_movies()
    tv_shows = fetch_tv_shows()
    books = fetch_books()
    combined_recommendations = movies + tv_shows + books
    if not combined_recommendations:
        return "No recommendations available at the moment. Please try again later."
    surprise_pick = random.choice(combined_recommendations)
    return f"Surprise! Here's something you might like:\n\nType: {surprise_pick['type']}\nTitle: {surprise_pick['title']}\nDescription: {surprise_pick['description']}"
