from openai import OpenAI
from models import Book,Movie,TVShow
from APIs import OPENAI_API_KEY
client = OpenAI(
  api_key=OPENAI_API_KEY
)

def get_recommendations(user_history, media_type):
    
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

# Function to get book recommendations based on user history
def get_book_recommendations():
    books = Book.query.all()
    book_titles = [book.title for book in books]
    user_history = ", ".join(book_titles)
    return get_recommendations(user_history, media_type="books")

# Function to get movie recommendations based on user history
def get_movie_recommendations():
    movies = Movie.query.all()
    movie_titles = [movie.title for movie in movies]
    user_history = ", ".join(movie_titles)
    return get_recommendations(user_history, media_type="movies")

# Function to get TV show recommendations based on user history
def get_tv_show_recommendations():
    tv_shows = TVShow.query.all()
    tv_show_titles = [tv_show.title for tv_show in tv_shows]
    user_history = ", ".join(tv_show_titles)
    return get_recommendations(user_history, media_type="TV shows")

