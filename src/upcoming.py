import requests
from src.APIs import TMDB_API_KEY, GOOGLE_BOOKS_API_KEY

# API Configuration
TMDB_API_KEY = TMDB_API_KEY
GOOGLE_BOOKS_API_KEY = GOOGLE_BOOKS_API_KEY


def get_upcoming_movies():
    """
    Fetch the top 5 upcoming movies from the TMDB API.

    Returns:
        list[dict]: A list of dictionaries, each containing the title and release date of an upcoming movie.
    """
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("results", [])[:5]  # Get top 5 results
        return [{"title": movie["title"], "release_date": movie["release_date"]} for movie in movies]
    else:
        print("Failed to fetch upcoming movies.")
        return []


def get_upcoming_tv_shows():
    """
    Fetch the top 5 upcoming TV shows currently on the air from the TMDB API.

    Returns:
        list[dict]: A list of dictionaries, each containing the name and first air date of an upcoming TV show.
    """
    url = f"https://api.themoviedb.org/3/tv/on_the_air?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        tv_shows = response.json().get("results", [])[:5]  # Get top 5 results
        return [{"name": show["name"], "first_air_date": show["first_air_date"]} for show in tv_shows]
    else:
        print("Failed to fetch upcoming TV shows.")
        return []


def get_upcoming_books():
    """
    Fetch the top 5 newest books based on the Google Books API.

    Returns:
        list[dict]: A list of dictionaries, each containing the title and published date of a book.
    """
    query = "new releases"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&orderBy=newest&maxResults=5&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get("items", [])
        return [{"title": book["volumeInfo"]["title"], "published_date": book["volumeInfo"].get("publishedDate", "Unknown")} for book in books]
    else:
        print("Failed to fetch upcoming books.")
        return []


def display_upcoming_releases():
    """
    Display the top 5 upcoming movies, TV shows, and books.

    Fetches data from respective APIs and prints formatted results for each category.
    """
    print("Upcoming Movies:")
    for movie in get_upcoming_movies():
        print(f"- {movie['title']} (Release Date: {movie['release_date']})")
    
    print("\nUpcoming TV Shows:")
    for show in get_upcoming_tv_shows():
        print(f"- {show['name']} (First Air Date: {show['first_air_date']})")
    
    print("\nUpcoming Books:")
    for book in get_upcoming_books():
        print(f"- {book['title']} (Published Date: {book['published_date']})")
