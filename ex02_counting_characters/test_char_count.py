import unittest
from ex02_counting_characters import char_count

class TestCountingCharacter(unittest.TestCase):

    def test_char_count_len(self):
        test_string = "abcdef"
        self.assertEqual(len(test_string), char_count.by_len(test_string))

    def test_char_count_native(self):
        test_string = "abcdef"
        self.assertEqual(len(test_string), char_count.by_counting(test_string))

    def test_char_count_reduce(self):
        test_string = "abcdef"
        self.assertEqual(len(test_string), char_count.by_reduce(test_string))

if __name__ == '__main__':
    unittest.main()
