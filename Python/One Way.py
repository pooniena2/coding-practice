# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pIe -> false
# pales. pale -> true
# pale. bale -> true
# pale. bake -> false

def oneWay(s1: str, s2: str):
    s1Index = 0
    s2Index = 0
    diff = False

    if len(s1) - len(s2) > 1 or len(s2) - len(s1) > 1:
        return False

    while s1Index < len(s1) - 1 and s2Index < len(s2) - 1:
        if s1[s1Index] == s2[s2Index]:
            s1Index = s1Index + 1
            s2Index = s2Index + 1
        elif not diff:
            diff = True
            if len(s1) == len(s2):
                s1Index += 1
                s2Index += 1
            elif len(s1) > len(s2):
                s1Index += 1
            elif len(s1) < len(s2):
                s2Index += 1
        else:
            print(False)
            return False

    print(True)
    return True


oneWay('pales', 'paless')
oneWay('pale', 'pIe')
oneWay('pale', 'bale')
oneWay('pale', 'bake')
