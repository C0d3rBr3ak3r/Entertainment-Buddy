"""
File: main.py
Author: Daksh Malhotra
Date Modified: 20 March 2024

Description: 
Main script for managing media (books, movies, TV shows) including 
searching, recommending, adding, viewing, and displaying upcoming releases.
"""

from src.models import *
from src.constants import *
from src.search import *
from src.recommendations import *
from src.upcoming import display_upcoming_releases
from src.surprise import surprise_me
from src.add import *
from src.view import *


def recommend():
    """
    Provides recommendations based on the user's choice of media type.

    This function allows the user to choose between recommendations for movies, TV shows, books, or specific titles.
    The function also offers a 'Surprise me' option, providing random recommendations. The user can exit the recommendations menu
    or return to the main menu based on their selection.

    Returns:
        None
    """
    print(logo)
    print(f"""
What do you need recommendations for {question_mark}
1. Movies
2. TV shows
3. Books
4. Recommendations based on some specific titles
5. Surprise me
6. Exit
""")
    choice = input("Enter your choice: ")
    if choice == '1':
        print(get_movie_recommendations())
    elif choice == '2':
        print(get_tv_show_recommendations())
    elif choice == '3':
        print(get_book_recommendations())
    elif choice == '4':
        print(get_specific_recommendations())
    elif choice == '5':
        print(surprise_me())
    elif choice == '6':
        main_menu()
    else:
        print(f"{cross} Invalid Choice, Please Try again")
        recommend()

    while True:
        choice = input("Press enter to exit: ")
        if choice == "":
            break
        else:
            continue


def search():
    """
    Searches for media (movie, TV show, or book) based on user input.

    This function allows the user to search for a specific movie, TV show, or book. 
    It displays the top 5 results based on the user's query and provides the option to exit or return to the main menu.

    Returns:
        None
    """
    print(logo)
    print("Welcome to the Media Search!")
    media_type = input("Search for (movie/tv/book): ").strip().lower()
    query = input("Enter the name of the media: ").strip()

    if media_type in ["movie", "tv"]:
        results = search_movies_or_tv(query, media_type)
    elif media_type == "book":
        results = search_books(query)
    else:
        print("Invalid media type. Please choose 'movie', 'tv', or 'book'.")
        search()

    # Limit to top 5 results
    top_results = results[:5]
    display_results(top_results, media_type)

    while True:
        choice = input("Press enter to exit: ")
        if choice == "":
            main_menu()
        else:
            print(f"{cross}")
            continue


def add_media():
    """
    Prompts the user to add new media (book, movie, or TV show) to the system.

    This function presents the user with options to add a book, movie, or TV show to the database.
    The user can choose to add more media or return to the main menu after completing an addition.

    Returns:
        None
    """
    print(logo)
    print(f"""
What would you like to add{question_mark}
1. Book
2. Movie
3. TV Show
4. Return to main menu
""")
    choice = (input("Enter choice (1-4): "))
    if choice == '1':
        add_book()
    elif choice == '2':
        add_movie()
    elif choice == '3':
        add_tvshow()
    elif choice == '4':
        main_menu()
    else:
        print("Invalid Choice")
        add_media()
    choice = input(f"Would you like to add more media{question_mark}(y/n)")
    if choice in 'yY':
        add_media()
    else:
        main_menu()


def main_menu():
    """
    Displays the main menu and handles navigation to different options.

    This function presents the user with options to navigate to the add media, view media, search for media, 
    get recommendations, view upcoming releases, or exit the program.

    Returns:
        None
    """
    while True:
        print(logo)
        print("""
1. Add Media
2. View Media
3. Search for something
4. Recommendations
5. Latest or Upcoming Releases
6. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_media()
        elif choice == "2":
            view_media()
        elif choice == '3':
            search()
        elif choice == '4':
            recommend()
        elif choice == '5':
            display_upcoming_releases()
        elif choice == "6":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
