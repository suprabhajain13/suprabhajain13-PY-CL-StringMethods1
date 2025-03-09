import unittest
from src.main.lab import (
    get_string_length,
    get_character_at_index,
    get_index_given_character,
    string_slicing,
    concatenate_strings,
    repeat_string,
    string_length,
    convert_to_uppercase,
    convert_to_lowercase
)

class TestStringMethods(unittest.TestCase):

    def test_get_string_length(self):
        self.assertEqual(get_string_length("Hello"), 5)
        self.assertEqual(get_string_length(""), 0)
        self.assertEqual(get_string_length("Python"), 6)

    def test_get_character_at_index(self):
        self.assertEqual(get_character_at_index("Hello", 0), 'H')
        self.assertEqual(get_character_at_index("Python", 3), 'h')
        self.assertEqual(get_character_at_index("World", 4), 'd')

    def test_get_index_given_character(self):
        # Test cases for get_index_given_character function
        self.assertEqual(get_index_given_character("Hello", 'e'), 1)
        self.assertEqual(get_index_given_character("Hello", 'o'), 4)
        self.assertEqual(get_index_given_character("Hello", 'x'), -1)
        self.assertEqual(get_index_given_character("", 'x'), -1)
        self.assertEqual(get_index_given_character("Hello", ''), -1)

    def test_string_slicing(self):
        # Test cases for string_slicing function
        self.assertEqual(string_slicing("Hello, Python!", 7, 12), "Python")
        self.assertEqual(string_slicing("Hello, Python!", 0, 4), "Hello")
        self.assertEqual(string_slicing("Hello, Python!", 13, 20), "!")

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "Python"), "Hello Python")
        self.assertEqual(concatenate_strings("Good", "morning"), "Good morning")

    def test_repeat_string(self):
        self.assertEqual(repeat_string("Hello ", 3), "Hello Hello Hello ")
        self.assertEqual(repeat_string("Python", 2), "PythonPython")

    def test_string_length(self):
        self.assertEqual(string_length("Hello"), 5)
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length("Python"), 6)

    def test_convert_to_uppercase(self):
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")
        self.assertEqual(convert_to_uppercase("Python"), "PYTHON")

    def test_convert_to_lowercase(self):
        self.assertEqual(convert_to_lowercase("HELLO"), "hello")
        self.assertEqual(convert_to_lowercase("Python"), "python")

if __name__ == '__main__':
    unittest.main()
