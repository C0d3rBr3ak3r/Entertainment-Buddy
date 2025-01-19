from models import session, Book, Movie, TVShow, BookStatus, WatchStatus
from constants import *
import os

def clear():
    os.system('cls')

def add_book():
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
def add_media():
    clear()
    print(logo)
    print(f"""
What would you like to add{question_mark}
1. Book
2. Movie
3. TV Show
4. Return to main menu
""")
    choice=(input("Enter choice (1-3): "))
    if choice=='1':
        add_book()
    elif choice=='2':
        add_movie()
    elif choice=='3':
        add_tvshow()
    elif choice=='4':
        main_menu()
    else:
        print("Invalid Choice")
        add_media()
    choice=input(f"Would you like to add more media{question_mark}(y/n)")
    if choice in 'yY':
        add_media()
    else:
        main_menu()

def view_media():
    clear()
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
    choice=input("Enter your choice: ")
    if choice=='1':
        view_plan_to()
    elif choice=='2':
        view_watching_reading
    elif choice=='3':
        view_watched_read()
    elif choice=='4':
        view_books()
    elif choice=='5':
        view_movie_tv()
    elif choice=='6':
        main_menu()
    else:
        print(f"{cross} Invalid input , Please try again ")
        view_media()




def view_movie_tv():
    movies = session.query(Movie).all()
    tv_shows=session.query(TVShow).all()
    clear()
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

    choice= input("Press enter to go back: ")
    if choice=='':
        view_media()
    else:
        view_movie_tv()

def view_plan_to():
    to_read=session.query(Book).filter(Book.status==BookStatus.Plan_to_read).all()
    to_watch_movie=session.query(Movie).filter(Movie.status==WatchStatus.Plan_to_watch)
    to_watch_tv=session.query(TVShow).filter(TVShow.status==WatchStatus.Plan_to_watch)
    clear()
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

    choice= input("Press enter to go back: ")
    if choice=='':
        view_media()
    else:
        view_books()
def view_watched_read():
    read=session.query(Book).filter(Book.status==BookStatus.Read).all()
    watched_movie=session.query(Movie).filter(Movie.status==WatchStatus.Watched).all()
    watched_tv=session.query(TVShow).filter(TVShow.status==WatchStatus.Watched).all()
    clear()
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

    choice= input("Press enter to go back: ")
    if choice=='':
        view_media()
    else:
        view_books()
def view_watching_reading():
    reading=session.query(Book).filter(Book.status==BookStatus.Reading).all()
    watching_movie=session.query(Movie).filter(Movie.status==WatchStatus.Watching).all()
    watching_tv=session.query(TVShow).filter(TVShow.status==WatchStatus.Watching).all()
    clear()
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

    choice= input("Press enter to go back")
    if choice=='':
        view_media()
    else:
        view_books()
        
def view_books():
    books = session.query(Book).all()
    clear()
    print(logo)
    if books:
        print("\n--- All Books ---")
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print(f"No books found.")

    choice= input("Press enter to go back")
    if choice=='':
        main_menu()
    else:
        view_books()
def main_menu():
    while True:
        
        print(logo)
        print("1. Add Media")
        print("2. View Media")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_media()
        elif choice == "2":
            view_media()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
