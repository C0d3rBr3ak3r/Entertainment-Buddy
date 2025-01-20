from openai import OpenAI
from models import *
from APIs import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def get_recommendations(user_history, media_type):
    """
    Generate recommendations for a given media type based on the user's history using OpenAi API

    Args:
        user_history (str): A string containing a list of media titles from the user's history.
        media_type (str): The type of media for which recommendations are requested (e.g., "books", "movies", "TV shows").

    Returns:
        str: A string containing recommendations for the specified media type.
    """
    prompt = f"Based on the following {media_type} history: {user_history}, recommend 5 {media_type} they might enjoy."
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system",
             "content": "You are an assistant that recommends media based on user preferences."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.to_dict()["content"]


def get_book_recommendations():
    """
    Get book recommendations based on the user's reading history.

    Fetches all books from the database, extracts their titles, and generates a recommendation list.

    Returns:
        str: A string containing book recommendations.
    """
    books = session.query(Book).all()
    book_titles = [book.title for book in books]
    user_history = ", ".join(book_titles)
    return get_recommendations(user_history, media_type="books")


def get_movie_recommendations():
    """
    Get movie recommendations based on the user's watch history.

    Fetches all movies from the database, extracts their titles, and generates a recommendation list.

    Returns:
        str: A string containing movie recommendations.
    """
    movies = session.query(Movie).all()
    movie_titles = [movie.title for movie in movies]
    user_history = ", ".join(movie_titles)
    return get_recommendations(user_history, media_type="movies")


def get_tv_show_recommendations():
    """
    Get TV show recommendations based on the user's watch history.

    Fetches all TV shows from the database, extracts their titles, and generates a recommendation list.

    Returns:
        str: A string containing TV show recommendations.
    """
    tv_shows = session.query(TVShow).all()
    tv_show_titles = [tv_show.title for tv_show in tv_shows]
    user_history = ", ".join(tv_show_titles)
    return get_recommendations(user_history, media_type="TV shows")


def get_specific_recommendations():
    """
    Get specific recommendations for a user-specified media type and input.

    Prompts the user to enter a media type (e.g., "books", "movies") and titles or genres for recommendations.

    Returns:
        str: A string containing specific recommendations for the entered media type and input.
    """
    media_type = input("Enter the media type for recommendations: ")
    user_input = input("Enter the titles (or genre) related to which you need recommendations: ")
    return get_recommendations(user_input, media_type)

