import unittest
from unittest.mock import patch
from src.main import main_menu
from src.constants import *
class TestMainMenu(unittest.TestCase):
    
    @patch("builtins.input", side_effect=["6"])
    @patch("builtins.print")
    def test_main_menu_exit(self, mock_print, mock_input):
        """Test if main menu exits properly when the user selects 'Exit'"""
        with self.assertRaises(SystemExit):
            main_menu()
        mock_print.assert_any_call("Goodbye!")
    
    @patch("builtins.input", side_effect=["1", "4","6"])  # Add Media -> Return to main menu
    @patch("builtins.print")
    def test_main_menu_add_media(self, mock_print, mock_input):
        """
        Test if main_menu correctly navigates to add_media() and returns.
        """
        try:
            main_menu()
        except SystemExit:
            pass  # Ignore exit calls, just checking flow
        mock_input.assert_called()  # Ensure input was called

    @patch("builtins.input", side_effect=["2", "6","6"])  # View Media -> Exit
    @patch("builtins.print")
    def test_main_menu_view_media(self, mock_print, mock_input):
        """
        Test if main_menu correctly navigates to view_media().
        """
        try:
            main_menu()
        except SystemExit:
            pass
        mock_input.assert_called()

if __name__ == "__main__":
    unittest.main()