#!/usr/bin/env python

import re

class AnagramChecker:

    def __init__(self, word1='', word2=''):
        self.word1 = word1
        self.word2 = word2

    def check(self):
        self.word1 = self.strip_non_alnum(self.word1)
        self.word2 = self.strip_non_alnum(self.word2)

        if len(self.word1) != len(self.word2):
            return False

        if self.word1 == self.word2:
            print(self.word1, self.word2)
            return True

        self.word1 = ''.join(sorted(self.word1))
        self.word2 = ''.join(sorted(self.word2))

        if self.word1 == self.word2:
            return True

        return False

    def strip_non_alnum(self, word):
        stripped = re.sub('[^A-Za-z0-9]', '', word)
        return stripped

def run():
    print "Enter two phrases to see if they are anagrams."
    first = raw_input('First word: ')
    second = raw_input('Second word: ')

    if AnagramChecker(first, second).check():
        print "{first} and {second} are anagrams".format(first=first, second=second)
    else:
        print "{first} and {second} are NOT anagrams".format(first=first, second=second)


if __name__ == '__main__':
    run()
