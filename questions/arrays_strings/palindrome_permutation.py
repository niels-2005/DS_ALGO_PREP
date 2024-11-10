import time
import unittest

# Question:
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:Tact Coa
# Output:True (permutations: "taco cat'; "atc o eta·; etc.)


def is_palindrome_permutation(phrase):
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

    def test_pal_perm(self):
        for [test_string, expected] in self.test_cases:
            assert is_palindrome_permutation(test_string) == expected


if __name__ == "__main__":
    unittest.main()
