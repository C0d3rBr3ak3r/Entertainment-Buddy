from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum

# Database setup
DATABASE_URL = "sqlite:///entertainment_buddy.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Enums
class BookStatus(enum.Enum):
    Read = "Read"
    Reading = "Reading"
    Plan_to_read = "Plan to read"

class WatchStatus(enum.Enum):
    Watched = "Watched"
    Watching = "Watching"
    Plan_to_watch = "Plan to watch"

# Models
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    author = Column(String(150))
    status = Column(Enum(BookStatus), nullable=False)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    director = Column(String(150))
    status = Column(Enum(WatchStatus), nullable=False)

class TVShow(Base):
    __tablename__ = "tvshows"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    status = Column(Enum(WatchStatus), nullable=False)

# Create tables
Base.metadata.create_all(engine)
