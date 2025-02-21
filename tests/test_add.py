import unittest
from unittest.mock import patch, MagicMock
from src.models import Book, Movie, TVShow, session,BookStatus, WatchStatus
from src.add import add_book, add_movie, add_tvshow

class TestAdd(unittest.TestCase):
    @patch("builtins.input", side_effect=["The Hobbit", "J.R.R. Tolkien", "Read"])
    @patch("src.models.session.add")
    @patch("src.models.session.commit")
    def test_add_book_valid(self, mock_commit, mock_add, mock_input):
        add_book()
        mock_add.assert_called_once()
        mock_commit.assert_called_once()
    
    @patch("builtins.input", side_effect=["Inception", "Christopher Nolan", "Watched"])
    @patch("src.models.session.add")
    @patch("src.models.session.commit")
    def test_add_movie_valid(self, mock_commit, mock_add, mock_input):
        add_movie()
        mock_add.assert_called_once()
        mock_commit.assert_called_once()
    
    @patch("builtins.input", side_effect=["Breaking Bad", "Vince Gilligan", "Watching"])
    @patch("src.models.session.add")
    @patch("src.models.session.commit")
    def test_add_tvshow_valid(self, mock_commit, mock_add, mock_input):
        add_tvshow()
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()