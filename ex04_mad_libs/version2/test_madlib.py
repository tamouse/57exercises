import unittest
from ex04_mad_libs.version2.madlib import MadLib

class TestMadLib(unittest.TestCase):
    def setUp(self):
        self.prompts = ['long', 'walk', 'short', 'pier']
        self.template = "Take a {long} {walk} off a {short} {pier}!"
        self.madlib = MadLib(self.template)

    def test_prompts_extraction(self):
        self.assertEqual(sorted(self.prompts), sorted(self.madlib.prompts()) )

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

    def test_unique_prompts(self):
        template = "This {a} should {a} have {a} all {a} the {a} same {a} words"
        madlib = MadLib(template)
        self.assertEqual(['a'], madlib.prompts())

        expected = "This BLAH should BLAH have BLAH all BLAH the BLAH same BLAH words"
        words = {'a': "BLAH"}
        self.assertEqual(expected, madlib.render(words))


if __name__ == '__main__':
    unittest.main()
