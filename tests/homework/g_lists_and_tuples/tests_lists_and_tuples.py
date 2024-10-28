import unittest

from src.homework.g_lists_and_tuples.lists import get_lowest_list_value_list, get_highest_list_value_list
from src.homework.g_lists_and_tuples.tuples import get_lowest_list_value_tuple, get_highest_list_value_tuple

class Test_Config(unittest.TestCase):

    #Lists
    def test_get_lowest_list_value_list(self):
        self.assertEqual(1, get_lowest_list_value_list([8, 10, 1, 50, 20]))

    def test_get_highest_list_value_list(self):
        self.assertEqual(50, get_highest_list_value_list([8, 10, 1, 50, 20]))

    #Tuples
    def test_get_lowest_list_value_tuple(self):
        self.assertEqual(1, get_lowest_list_value_tuple((8, 10, 1, 50, 20)))

    def test_get_highest_list_value_tuple(self):
        self.assertEqual(50, get_highest_list_value_tuple((8, 10, 1, 50, 20)))
