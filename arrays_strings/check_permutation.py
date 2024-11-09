import time
import unittest


# Question:
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def check_permutation(s1: str, s2: str) -> bool:
    return True


class Test(unittest.TestCase):
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    def test_string_compression(self):
            for string1, string2, expected in self.test_cases:
                assert check_permutation(string1, string2) == expected



if __name__ == "__main__":
    unittest.main()
