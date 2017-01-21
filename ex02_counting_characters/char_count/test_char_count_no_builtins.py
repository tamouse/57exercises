import unittest
from ex02_counting_characters.char_count.char_count_no_builtins import CharCount


class TestCharCount(unittest.TestCase):
    def setUp(self):
        self.counter = CharCount()

    def test_count(self):
        self.assertEqual(len('test string'), self.counter.count('test string'))

    def test_count_empty_string(self):
        self.assertEqual(0, self.counter.count(''))

    def test_count_one_char(self):
        self.assertEqual(1, self.counter.count(' '))
