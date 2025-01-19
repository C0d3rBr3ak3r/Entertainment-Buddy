import requests

# API Keys
TMDB_API_KEY = "fd0e53fdf7441eff0562a073432e28d8"  
GOOGLE_BOOKS_API_KEY = "AIzaSyDm_CX8sctKOjNCNeFdaVQLqKGI-cm3n80"  

# Base URLs for APIs
TMDB_BASE_URL = "https://api.themoviedb.org/3"
GOOGLE_BOOKS_BASE_URL = "https://www.googleapis.com/books/v1/volumes"

def search_movies_or_tv(query, media_type="movie"):
    """
    Search for movies or TV shows using the TMDb API.
    
    Args:
        query (str): The search term.
        media_type (str): Type of media ('movie' or 'tv').
    
    Returns:
        list: A list of search results with title and other details.
    """
    endpoint = f"{TMDB_BASE_URL}/search/{media_type}"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "en-US",
        "page": 1,
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def search_books(query):
    """
    Search for books using the Google Books API.
    
    Args:
        query (str): The search term.
    
    Returns:
        list: A list of search results with book titles and details.
    """
    params = {
        "q": query,
        "key": GOOGLE_BOOKS_API_KEY,
        "maxResults": 10,  # Limit results
    }
    response = requests.get(GOOGLE_BOOKS_BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def display_results(results, media_type):
    """
    Display search results in a readable format.
    
    Args:
        results (list): List of search results.
        media_type (str): Type of media ('movie', 'tv', or 'book').
    """
    if not results:
        print("No results found.")
        return

    print(f"\nSearch Results for {media_type.capitalize()}:\n")
    for i, result in enumerate(results, start=1):
        if media_type in ["movie", "tv"]:
            title = result.get("title") or result.get("name")
            release_date = result.get("release_date") or result.get("first_air_date", "Unknown")
            overview = result.get("overview", "No description available.")
            print(f"{i}. {title} ({release_date})\n   {overview}\n")
        elif media_type == "book":
            volume_info = result.get("volumeInfo", {})
            title = volume_info.get("title", "Unknown Title")
            authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
            description = volume_info.get("description", "No description available.")
            print(f"{i}. {title} by {authors}\n   {description}\n")
