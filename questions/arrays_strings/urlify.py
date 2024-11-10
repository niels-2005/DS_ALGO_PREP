import time
import unittest

# Question:
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters,and that you are given the "true"
# length of the string.


def ulify_algorithm(string: str, length: int) -> str:
    return True


def ulify_algorithm_pythonic(string: str, length: int) -> str:
    return True


class Test(unittest.TestCase):

    test_functions = [ulify_algorithm, ulify_algorithm_pythonic]

    test_cases = {
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
        ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
        (" a b    ", 4, "%20a%20b"),
        (" a b       ", 5,"%20a%20b%20"),
    }

    def test_urlify(self):
        for test_function in self.test_functions:
            for string, length, expected in self.test_cases:
                assert test_function(string, length) == expected


if __name__ == "__main__":
    unittest.main()
