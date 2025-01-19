from models import *
from main import session
from constants import *

def add_book():
    """
    Prompts the user to enter information about a book (title, author, status) and adds it to the database.

    The function validates the entered status and attempts to add a new book to the database. 
    If the status is invalid, it will notify the user and prompt for a retry. 
    If an error occurs during the database operation, the error message will be displayed.

    The valid statuses for the book are 'Read', 'Reading', and 'Plan to Read'.
    """
    title = input("Enter book title: ")
    author = input("Enter author: ")
    status = input("Enter status (Read/Reading/Plan to Read): ")

    try:
        book_status = BookStatus[status.replace(" ", "_")]
        new_book = Book(title=title, author=author, status=book_status)
        session.add(new_book)
        session.commit()
        print(f"Book '{title}' added successfully!")
    except KeyError:
        print(f"{cross} Invalid status. Please enter 'Read', 'Reading', or 'Plan to read'.")
        print("Please Retry !")
        add_book()
    except Exception as e:
        print(f"Error: {e}")

def add_movie():
    """
    Prompts the user to enter information about a movie (title, director, status) and adds it to the database.

    The function validates the entered status and attempts to add a new movie to the database. 
    If the status is invalid, it will notify the user and prompt for a retry. 
    If an error occurs during the database operation, the error message will be displayed.

    The valid statuses for the movie are 'Watched', 'Watching', and 'Plan to Watch'.
    """
    title = input("Enter Movie title: ")
    director = input("Enter director: ")
    status = input("Enter status (Watched/Watching/Plan to Watch): ")

    try:
        movie_status = WatchStatus[status.replace(" ", "_")]
        new_movie = Movie(title=title, director=director, status=movie_status)
        session.add(new_movie)
        session.commit()
        print(f"Movie '{title}' added successfully!")
    except KeyError:
        print(f"{cross} Invalid status. Please enter 'Watched', 'Watching', or 'Plan to watch'.")
        print("Please Retry !")
        add_movie()
    except Exception as e:
        print(f"Error: {e}")

def add_tvshow():
    """
    Prompts the user to enter information about a TV show (title, director, status) and adds it to the database.

    The function validates the entered status and attempts to add a new TV show to the database. 
    If the status is invalid, it will notify the user and prompt for a retry. 
    If an error occurs during the database operation, the error message will be displayed.

    The valid statuses for the TV show are 'Watched', 'Watching', and 'Plan to Watch'.
    """
    title = input("Enter Movie title: ")
    director = input("Enter director: ")
    status = input("Enter status (Watched/Watching/Plan to Watch): ")

    try:
        tvshow_status = WatchStatus[status.replace(" ", "_")]
        new_movie = TVShow(title=title, director=director, status=tvshow_status)
        session.add(new_movie)
        session.commit()
        print(f"TV Show '{title}' added successfully!")
    except KeyError:
        print(f"{cross} Invalid status. Please enter 'Watch', 'Watching', or 'Plan to Watch'.")
        print("Please Retry !")
        add_tvshow()
    except Exception as e:
        print(f"Error: {e}")
