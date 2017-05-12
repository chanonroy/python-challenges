'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
'''

def find_missing_letter(chars):
    ascii_val = ord(chars[0])

    for index, c in enumerate(chars):

        if index == 0:
            continue

        diff = ord(c) - ascii_val

        if diff > 1:
           return chr(ord(c) - 1)

        ascii_val = ord(c)
