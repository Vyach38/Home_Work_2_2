import unittest
from utils import dicts


class TestUnit(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: "Hello", 2: "World"}, 1), "Hello")
        self.assertEqual(dicts.get_val({1: "Hello", 2: "World"}, 2), "World")
        self.assertEqual(dicts.get_val({1: "Hello", 2: "World"}, 0), "git")
        self.assertEqual(dicts.get_val({}, 1), "git")
