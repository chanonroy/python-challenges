"""Anagram: rearrange letters of word1 get word 2."""

"""
firstWords = array with word 1
secondWords = array with word 2
return print 1 for anagram, 0 if not
"""

firstWords = ['cinema', 'host', 'aba', 'train']
secondWords = ['iceman', 'shot', 'bab', 'rain']


def anagram(firstWords, secondWords):

    words = zip(firstWords, secondWords)

    for x in words:
        anagram = 0

        c1 = [0]*26
        c2 = [0]*26

        s1 = x[0]
        s2 = x[1]

        if len(s1) != len(s2):
            anagram = 0
        else:
            for i in range(len(s1)):
                pos = ord(s1[i]) - ord('a')
                c1[pos] = c1[pos] + 1

            for i in range(len(s2)):
                pos = ord(s2[i]) - ord('a')
                c2[pos] = c2[pos] + 1

            if c2 == c1:
                anagram = 1
            else:
                anagram = 0

        print anagram


result = anagram(firstWords, secondWords)
