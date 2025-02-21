from src.models import *
from src.constants import *

def view_movie_tv():
    """
    Retrieves and displays all movies and TV shows from the database.
    
    This function queries the database to retrieve all movies and TV shows, and then prints their details (ID, title, director, and status).
    If no movies or TV shows are found, appropriate messages are displayed. The user can press enter to return to the previous menu.
    """
    movies = session.query(Movie).all()
    tv_shows = session.query(TVShow).all()
    print(logo)
    if movies:
        print("\n--- All Movies ---")
        for movie in movies:
            print(f"ID: {movie.id}, Title: {movie.title}, Director: {movie.director}, Status: {movie.status.value}")
    else:
        print(f"{cross} No Movies found.")

    if tv_shows:
        print("\n--- All TV Shows ---")
        for tv_show in tv_shows:
            print(f"ID: {tv_show.id}, Title: {tv_show.title}, Director: {tv_show.director}, Status: {tv_show.status.value}")
    else:
        print(f"{cross} No TV shows found.")

    choice = input("Press enter to go back: ")
    if choice == '':
        view_media()
    else:
        view_movie_tv()

def view_plan_to():
    """
    Displays items that are planned to be watched or read (status: 'Plan to Read' or 'Plan to Watch').

    This function retrieves books with the 'Plan to Read' status, movies, and TV shows with the 'Plan to Watch' status from the database.
    It prints the details of the items found. If no items match the status, an appropriate message is shown.
    The user can press enter to return to the previous menu.
    """
    to_read = session.query(Book).filter(Book.status == BookStatus.Plan_to_read).all()
    to_watch_movie = session.query(Movie).filter(Movie.status == WatchStatus.Plan_to_watch).all()
    to_watch_tv = session.query(TVShow).filter(TVShow.status == WatchStatus.Plan_to_watch).all()

    print(logo)
    if to_read:
        print("----------PLAN TO READ-----------")
        for book in to_read:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print(f"{cross} No books to read")

    if to_watch_movie or to_watch_tv:
        print("----------PLAN TO WATCH-----------")
        for media in to_watch_movie:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
        for media in to_watch_tv:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
    else:
        print(f"{cross} No media to watch")

    choice = input("Press enter to go back: ")
    if choice == '':
        view_media()
    else:
        view_books()

def view_watched_read():
    """
    Displays items that are watched or read (status: 'Read' or 'Watched').

    This function retrieves books with the 'Read' status, movies, and TV shows with the 'Watched' status from the database.
    It prints the details of the items found. If no items match the status, an appropriate message is shown.
    The user can press enter to return to the previous menu.
    """
    read = session.query(Book).filter(Book.status == BookStatus.Read).all()
    watched_movie = session.query(Movie).filter(Movie.status == WatchStatus.Watched).all()
    watched_tv = session.query(TVShow).filter(TVShow.status == WatchStatus.Watched).all()

    print(logo)
    if read:
        print("----------READ-----------")
        for book in read:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print(f"{cross} No books read")

    if watched_movie or watched_tv:
        print("----------WATCHED-----------")
        for media in watched_movie:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
        for media in watched_tv:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
    else:
        print(f"{cross} No media watched")

    choice = input("Press enter to go back: ")
    if choice == '':
        view_media()
    else:
        view_books()

def view_watching_reading():
    """
    Displays items that are being watched or read (status: 'Reading' or 'Watching').

    This function retrieves books with the 'Reading' status, movies, and TV shows with the 'Watching' status from the database.
    It prints the details of the items found. If no items match the status, an appropriate message is shown.
    The user can press enter to return to the previous menu.
    """
    reading = session.query(Book).filter(Book.status == BookStatus.Reading).all()
    watching_movie = session.query(Movie).filter(Movie.status == WatchStatus.Watching).all()
    watching_tv = session.query(TVShow).filter(TVShow.status == WatchStatus.Watching).all()

    print(logo)
    if reading:
        print("----------READING-----------")
        for book in reading:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print(f"{cross} No books reading")

    if watching_movie or watching_tv:
        print("----------WATCHING-----------")
        for media in watching_movie:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
        for media in watching_tv:
            print(f"ID: {media.id}, Title: {media.title}, Director: {media.director}, Status: {media.status.value}")
    else:
        print(f"{cross} No media watching")

    choice = input("Press enter to go back")
    if choice == '':
        view_media()
    else:
        view_books()

def view_books():
    """
    Displays all books in the database.

    This function retrieves all books from the database and prints their details (ID, title, author, and status).
    If no books are found, a message indicating that no books were found will be displayed.
    The user can press enter to return to the previous menu.
    """
    books = session.query(Book).all()
    print(logo)
    if books:
        print("\n--- All Books ---")
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print(f"No books found.")

    choice = input("Press enter to go back")
    if choice == '':
        view_media()
    else:
        view_books()

def view_media():
    """
    Displays a menu for the user to choose how they would like to view media items (books, movies, TV shows).

    This function presents the user with a list of options for viewing items by status (Plan to Watch/Read, Watching/Reading, Watched/Read), 
    or by type (Books, Movies, TV Shows). The user can select an option to view items accordingly.
    The user can also choose to exit to the main menu.
    """
    print(logo)
    print(f"""
How would you like to view items {question_mark}
1. Plan to watch/read
2. Watching/Reading
3. Watched/Read
4. Books
5. Movies and TV shows
6. Exit to main menu
""")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_plan_to()
    elif choice == '2':
        view_watching_reading()
    elif choice == '3':
        view_watched_read()
    elif choice == '4':
        view_books()
    elif choice == '5':
        view_movie_tv()
    elif choice == '6':
        pass
    else:
        print(f"{cross} Invalid input , Please try again ")
        view_media()
