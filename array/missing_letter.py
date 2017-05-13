"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Examples:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

import unittest


def missing_letter(chars):

    # Find base ascii value to use as counter
    ascii_val = ord(chars[0])

    for index, c in enumerate(chars):

        if index == 0:
            continue

        current_val = ord(c)

        diff = current_val - ascii_val

        if diff > 1:
            # Skipped a letter, find out what that letter was
            return chr(current_val - 1)

        # Difference okay, set counter to current value
        ascii_val = current_val


# Unit Testing
class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(missing_letter(['a','b','c','d','f']), 'e')

    def test2(self):
        self.assertEqual(missing_letter(['O','Q','R','S']), 'P')


if __name__ == '__main__':
    unittest.main()
