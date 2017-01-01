
import unittest
from ex24_anagram_checker.anagram_checker import AnagramChecker

class AnagramCheckerTestCase(unittest.TestCase):

    def test_two_anagrams(self):
        word1='hello'
        word2='o hell'
        ac=AnagramChecker(word1, word2)
        self.assertTrue(ac.check())
