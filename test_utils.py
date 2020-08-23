'''
This module demonstrates testing for functions in the utils module.
'''
import unittest
from utils import *
class Testutils(unittest.TestCase):

    def setUp(self):
          ''' Initalizes the expectation from the test'''
          self.expected_menu_response_one = 1
          self.expected_menu_response_two = "Please input a value between 0 and 2"
          self.expected_name_response = "Bob"
          self.total_prices =350.0
          self.total_prices_dict = {"AIG":175.0, "XR": 175.0}
    def test_display_menu(self):
        expected = self.expected_menu_response_one
        # expected = self.expected_menu_response_two
        actual_execution = display_menu()
        self.assertEqual(actual_execution, expected)

    def test_accept_name(self):
        expected = self.expected_name_response
        actual_execution = accept_name()
        self.assertEqual(actual_execution, expected)
    def test_calculate_total_price(self):
        expected =self.total_prices
        actual_execution = calculate_total_price(self.total_prices_dict)
        self.assertEqual(expected, actual_execution)


if __name__ == "__main__":
    unittest.main()
