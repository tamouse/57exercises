import unittest
from ex04_mad_libs.madlib import MadLib

class TestMadLib(unittest.TestCase):

    def test_render(self):
        words = {'noun': "dog", 'adjective': "blue"}
        template = "I walked my {adjective} {noun} yesterday"
        expected = "I walked my blue dog yesterday"

        self.assertEqual(expected, MadLib([], template).render(words))

    def test_next_prompt(self):
        prompts = ["noun", "adjective"]
        madlib = MadLib(prompts, '')

        self.assertEqual(prompts[0], madlib.next_prompt())
        self.assertEqual(prompts[1], madlib.next_prompt())

    def test_full_cycle(self):
        prompts = ["noun", "adjective"]
        template = "I walked my {adjective} {noun} yesterday"
        expected = "I walked my blue dog yesterday"

        madlib = MadLib(prompts, template)

        words = {}
        words[madlib.next_prompt()] = 'dog'
        words[madlib.next_prompt()] = 'blue'

        self.assertEqual({'noun': 'dog', 'adjective': 'blue'}, words )
        self.assertEqual(expected, madlib.render(words))


if __name__ == '__main__':
    unittest.main()
