import unittest
from unittest.mock import patch, MagicMock
from src.recommendations import (
    get_recommendations,
    get_book_recommendations,
    get_movie_recommendations,
    get_tv_show_recommendations,
    get_specific_recommendations
)
from src.models import Book, Movie, TVShow

class TestRecommendations(unittest.TestCase):
    
    @patch("src.recommendations.client.chat.completions.create")
    def test_get_recommendations(self, mock_openai):
        mock_openai.return_value.choices = [MagicMock(message=MagicMock(to_dict=lambda: {"content": "Recommended Book 1, Recommended Book 2"}))]
        result = get_recommendations("Book A, Book B", "books")
        self.assertIn("Recommended Book 1", result)
    
    @patch("src.recommendations.session.query")
    @patch("src.recommendations.client.chat.completions.create")
    def test_get_book_recommendations(self, mock_openai, mock_query):
        mock_openai.return_value.choices = [MagicMock(message=MagicMock(to_dict=lambda: {"content": "Book X, Book Y"}))]
        mock_query.return_value.all.return_value = [Book(title="Book A"), Book(title="Book B")]
        result = get_book_recommendations()
        self.assertIn("Book X", result)
    
    @patch("src.recommendations.session.query")
    @patch("src.recommendations.client.chat.completions.create")
    def test_get_movie_recommendations(self, mock_openai, mock_query):
        mock_openai.return_value.choices = [MagicMock(message=MagicMock(to_dict=lambda: {"content": "Movie X, Movie Y"}))]
        mock_query.return_value.all.return_value = [Movie(title="Movie A"), Movie(title="Movie B")]
        result = get_movie_recommendations()
        self.assertIn("Movie X", result)
    
    @patch("src.recommendations.session.query")
    @patch("src.recommendations.client.chat.completions.create")
    def test_get_tv_show_recommendations(self, mock_openai, mock_query):
        mock_openai.return_value.choices = [MagicMock(message=MagicMock(to_dict=lambda: {"content": "TV Show X, TV Show Y"}))]
        mock_query.return_value.all.return_value = [TVShow(title="TV Show A"), TVShow(title="TV Show B")]
        result = get_tv_show_recommendations()
        self.assertIn("TV Show X", result)
    
    @patch("builtins.input", side_effect=["movies", "Action, Thriller"])
    @patch("src.recommendations.client.chat.completions.create")
    def test_get_specific_recommendations(self, mock_openai, mock_input):
        mock_openai.return_value.choices = [MagicMock(message=MagicMock(to_dict=lambda: {"content": "Movie A, Movie B"}))]
        result = get_specific_recommendations()
        self.assertIn("Movie A", result)

if __name__ == "__main__":
    unittest.main()
