import unittest
from unittest.mock import patch
from src.surprise import fetch_movies, fetch_tv_shows, fetch_books, surprise_me

class TestSurprise(unittest.TestCase):
    @patch('src.surprise.requests.get')
    def test_fetch_movies(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [{"title": "Movie1", "overview": "Description1"}]}
        self.assertEqual(fetch_movies(), [{"type": "Movie", "title": "Movie1", "description": "Description1"}])
    
    @patch('src.surprise.requests.get')
    def test_fetch_tv_shows(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [{"name": "Show1", "overview": "Description1"}]}
        self.assertEqual(fetch_tv_shows(), [{"type": "TV Show", "title": "Show1", "description": "Description1"}])
    
    @patch('src.surprise.requests.get')
    def test_fetch_books(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"volumeInfo": {"title": "Book1", "description": "Description1"}}]}
        self.assertEqual(fetch_books(), [{"type": "Book", "title": "Book1", "description": "Description1"}])
    
    @patch('src.surprise.fetch_movies', return_value=[{"type": "Movie", "title": "Movie1", "description": "Description1"}])
    @patch('src.surprise.fetch_tv_shows', return_value=[])
    @patch('src.surprise.fetch_books', return_value=[])
    def test_surprise_me(self, mock_movies, mock_tv, mock_books):
        result = surprise_me()
        self.assertIn("Movie1", result)

if __name__ == '__main__':
    unittest.main()
