import unittest

from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_option_ratio(self):
        self.assertEqual(0.25, get_options_ratio(5, 20))
        self.assertEqual(0.5, get_options_ratio(10, 20))

    def test_get_faculty_rating(self):
        self.assertEqual("error", get_faculty_rating(1.000001))
        self.assertEqual("Perfect", get_faculty_rating(1))
        self.assertEqual("Excellent", get_faculty_rating(.99999999999))
        self.assertEqual("Excellent", get_faculty_rating(.900001))
        self.assertEqual("Very Good", get_faculty_rating(.9))
        self.assertEqual("Very Good", get_faculty_rating(.8000001))
        self.assertEqual("Good", get_faculty_rating(.8))
        self.assertEqual("Good", get_faculty_rating(.70000001))
        self.assertEqual("Needs Improvement", get_faculty_rating(.7))
        self.assertEqual("Needs Improvement", get_faculty_rating(.600000001))
        self.assertEqual("Unacceptable", get_faculty_rating(.6))
        self.assertEqual("Unacceptable", get_faculty_rating(.5))
        self.assertEqual("Unacceptable", get_faculty_rating(.3))
        self.assertEqual("Unacceptable", get_faculty_rating(.2))
        self.assertEqual("Unacceptable", get_faculty_rating(.1))
        self.assertEqual("Unacceptable", get_faculty_rating(.00001))
        self.assertEqual("error", get_faculty_rating(-1))

