import unittest
from unittest.mock import patch
from src.upcoming import get_upcoming_movies, get_upcoming_tv_shows, get_upcoming_books

class TestUpcoming(unittest.TestCase):
    
    @patch("src.upcoming.requests.get")
    def test_get_upcoming_movies(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [
            {"title": "Movie 1", "release_date": "2025-05-20"},
            {"title": "Movie 2", "release_date": "2025-06-15"}
        ]}
        result = get_upcoming_movies()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("title", result[0])
        self.assertIn("release_date", result[0])
    
    @patch("src.upcoming.requests.get")
    def test_get_upcoming_tv_shows(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [
            {"name": "Show 1", "first_air_date": "2025-07-10"},
            {"name": "Show 2", "first_air_date": "2025-08-22"}
        ]}
        result = get_upcoming_tv_shows()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("name", result[0])
        self.assertIn("first_air_date", result[0])
    
    @patch("src.upcoming.requests.get")
    def test_get_upcoming_books(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [
            {"volumeInfo": {"title": "Book 1", "publishedDate": "2025-04-05"}},
            {"volumeInfo": {"title": "Book 2", "publishedDate": "2025-09-12"}}
        ]}
        result = get_upcoming_books()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("title", result[0])
        self.assertIn("published_date", result[0])

if __name__ == "__main__":
    unittest.main()
