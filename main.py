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
        print("Invalid status. Please enter 'Read', 'Reading', or 'Plan to read'.")
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
        print("Invalid status. Please enter 'Watched', 'Watching', or 'Plan to watch'.")
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
        print(f"Movie '{title}' added successfully!")
    except KeyError:
        print("Invalid status. Please enter 'Watch', 'Watching', or 'Plan to Watch'.")
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
    choice=int(input("Enter choice (1-3): "))
    if choice==1:
        add_book()
    elif choice==2:
        add_movie()
    elif choice==3:
        add_tvshow()
    elif choice==4:
        main_menu()
    else:
        print("Invalid Choice")
        add_media()
    choice=input(f"Would you like to add more media{question_mark}(y/n)")
    if choice in 'yY':
        add_media()
    else:
        main_menu()


def view_books():
    books = session.query(Book).all()
    clear()
    print(logo)
    if books:
        print("\n--- All Books ---")
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {book.status.value}")
    else:
        print("No books found.")

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
            view_books()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
