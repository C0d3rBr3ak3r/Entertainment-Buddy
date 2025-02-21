import unittest
from unittest.mock import patch, MagicMock
from src.view import *

class TestViewMedia(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['','6'])
    @patch('src.view.session.query')
    def test_view_movie_tv_no_data(self, mock_query, mock_input):
        mock_query.side_effect = [MagicMock(all=MagicMock(return_value=[])), 
                                  MagicMock(all=MagicMock(return_value=[]))]
        view_movie_tv()

    @patch('builtins.input', side_effect=['','6'])
    @patch('src.view.session.query')
    def test_view_plan_to_no_data(self, mock_query, mock_input):
        mock_query.side_effect = [MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[]))))]
        view_plan_to()

    @patch('builtins.input', side_effect=['','6'])
    @patch('src.view.session.query')
    def test_view_watched_read_no_data(self, mock_query, mock_input):
        mock_query.side_effect = [MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[]))))]
        view_watched_read()

    @patch('builtins.input', side_effect=['','6'])
    @patch('src.view.session.query')
    def test_view_watching_reading_no_data(self, mock_query, mock_input):
        mock_query.side_effect = [MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))),
                                  MagicMock(filter=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[]))))]
        view_watching_reading()

    @patch('builtins.input', side_effect=['','6'])
    @patch('src.view.session.query')
    def test_view_books_no_data(self, mock_query, mock_input):
        mock_query.return_value.all.return_value = []
        view_books()

if __name__ == '__main__':
    unittest.main()
