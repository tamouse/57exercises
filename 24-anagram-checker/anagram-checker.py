"""

Read two words from input, and check to see if they are anagrams.

"""

import re

def isAnagram(first, second):
    print "Checking '" + first + "' against '" + second + "'"

    # strip non-alphanumerics
    first  = re.sub('[^A-Za-z0-9]', '', first)
    second = re.sub('[^A-Za-z0-9]', '', second)

    if len(first) != len(second):
        print "False: '%s' != '%s' different lengths" % (first, second)
        return False

    if first == second:
        print "True: '%s' == '%s' same string of letters" % (first, second)
        return True

    # first_l = list(first)
    # second_l = list(second)

    # # Why are some methods called with dot notation,
    # # while others are called procedurally??
    # first_l.sort()
    # second_l.sort()

    # # This feels TOTALLY backwards!!
    # first = ''.join(first_l)
    # second = ''.join(second_l)

    # Maybe better?
    first = ''.join(sorted(first))
    second = ''.join(sorted(second))

    if first == second:
        print "True: '%s' == '%s' same string of letters after sorting" % (first, second)
        return True

    return False


print isAnagram('o n; e', 'e ! n $ o')

print "Enter two phrases to see if thay are anagrams."
first = raw_input('First word: ')
second = raw_input('Second word: ')

if isAnagram(first, second):
    print "They are anagrames"
else:
    print "They are NOT anagrams"
