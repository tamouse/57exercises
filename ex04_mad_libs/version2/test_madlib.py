import unittest
from ex04_mad_libs.version2.madlib import MadLib

class TestMadLib(unittest.TestCase):
    def setUp(self):
        self.template = "Take a {long} {walk} off a {short} {pier}!"
        self.madlib = MadLib(self.template)

    def test_prompts_extraction(self):
        self.assertEqual(['long', 'walk', 'short', 'pier'], self.madlib.prompts() )

    def test_prompts_iter(self):
        self.assertEqual('long', next(self.madlib.prompts_iter()) )
        self.assertEqual('walk', next(self.madlib.prompts_iter()) )
        self.assertEqual('short', next(self.madlib.prompts_iter()) )
        self.assertEqual('pier', next(self.madlib.prompts_iter()) )
        with self.assertRaises(StopIteration):
            next(self.madlib.prompts_iter())

    def test_render(self):
        words = {
            'long': "LONG",
            'walk': "WALK",
            'short': "SHORT",
            'pier': "PIER"
        }
        expected = "Take a LONG WALK off a SHORT PIER!"
        self.assertEqual(expected, self.madlib.render(words))

    def test_full_cycle(self):
        words = {}
        for prompt in self.madlib.prompts():
            words[prompt] = prompt.upper()
        expected = "Take a LONG WALK off a SHORT PIER!"
        self.assertEqual(expected, self.madlib.render(words))


if __name__ == '__main__':
    unittest.main()
