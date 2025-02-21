import unittest
from unittest.mock import patch
from src.search import search_movies_or_tv, search_books, display_results

class TestSearch(unittest.TestCase):
    
    @patch("src.search.requests.get")
    def test_search_movies_or_tv(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [{"title": "Test Movie", "release_date": "2024-01-01", "overview": "A test movie."}]}
        
        results = search_movies_or_tv("Test")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]["title"], "Test Movie")

    @patch("src.search.requests.get")
    def test_search_books(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"volumeInfo": {"title": "Test Book", "authors": ["Author Name"], "description": "A test book."}}]}
        
        results = search_books("Test")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]["volumeInfo"]["title"], "Test Book")

    def test_display_results_movies(self):
        test_data = [{"title": "Test Movie", "release_date": "2024-01-01", "overview": "A test movie."}]
        try:
            display_results(test_data, "movie")
        except Exception as e:
            self.fail(f"display_results raised an exception: {e}")

    def test_display_results_books(self):
        test_data = [{"volumeInfo": {"title": "Test Book", "authors": ["Author Name"], "description": "A test book."}}]
        try:
            display_results(test_data, "book")
        except Exception as e:
            self.fail(f"display_results raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
