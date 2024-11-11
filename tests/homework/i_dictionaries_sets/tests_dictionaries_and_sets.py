import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        self.assertEqual({"Widget1":10}, add_inventory({}, "Widget1", 10))
        self.assertEqual({"Widget1":35}, add_inventory({"Widget1":10}, "Widget1", 25))
        self.assertEqual({"Widget1":25}, add_inventory({"Widget1":35}, "Widget1", -10))

    def test_remove_inventory_widget(self):
        self.assertEqual({}, remove_inventory_widget({"Widget1":10}, "Widget1"))
