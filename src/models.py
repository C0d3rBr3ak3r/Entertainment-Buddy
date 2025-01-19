from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum

# Database setup
DATABASE_URL = "sqlite:///entertainment_buddy.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Enums
class BookStatus(enum.Enum):
    """
    Enumeration for book statuses.

    Attributes:
        Read (str): Indicates the book has been read.
        Reading (str): Indicates the book is currently being read.
        Plan_to_read (str): Indicates the book is planned to be read.
    """
    Read = "Read"
    Reading = "Reading"
    Plan_to_read = "Plan to read"


class WatchStatus(enum.Enum):
    """
    Enumeration for watch statuses.

    Attributes:
        Watched (str): Indicates the content has been watched.
        Watching (str): Indicates the content is currently being watched.
        Plan_to_watch (str): Indicates the content is planned to be watched.
    """
    Watched = "Watched"
    Watching = "Watching"
    Plan_to_watch = "Plan to watch"


# Models
class Book(Base):
    """
    ORM model for books.

    Attributes:
        id (int): Primary key for the book.
        title (str): Title of the book (unique and non-nullable).
        author (str): Author of the book (nullable).
        status (Enum): Current reading status of the book (non-nullable).
    """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    author = Column(String(150))
    status = Column(Enum(BookStatus), nullable=False)


class Movie(Base):
    """
    ORM model for movies.

    Attributes:
        id (int): Primary key for the movie.
        title (str): Title of the movie (unique and non-nullable).
        director (str): Director of the movie (nullable).
        status (Enum): Current watch status of the movie (non-nullable).
    """
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    director = Column(String(150), nullable=True)
    status = Column(Enum(WatchStatus), nullable=False)


class TVShow(Base):
    """
    ORM model for TV shows.

    Attributes:
        id (int): Primary key for the TV show.
        title (str): Title of the TV show (unique and non-nullable).
        director (str): Director of the TV show (nullable).
        status (Enum): Current watch status of the TV show (non-nullable).
    """
    __tablename__ = "tvshows"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    director = Column(String(150), nullable=True)
    status = Column(Enum(WatchStatus), nullable=False)


# Create tables
Base.metadata.create_all(engine)
