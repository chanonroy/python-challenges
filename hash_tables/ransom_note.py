# Can you make a replica of a ransom note with magazine words?

magazine = 'wi z ne we ebixk yvrd qrd ojckw q'
ransom = 'dwuu tvic y dnapw ujj tidi nstms x xe'


def canConstruct(ransom, magazine):
    """
    ransomNote: str
    magazine: str
    return: bool
    """

    for i in set(ransom):
        if ransom.count(i) > magazine.count(i):
            return False
        return True


print(canConstruct(ransom, magazine))

# fails certain hacker rank tests casts TODO: revisit this
