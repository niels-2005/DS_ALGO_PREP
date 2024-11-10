import time
import unittest

# Question:
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique_string(string: str) -> bool:
    # CODE HERE, allowed Data Structures
    return True


def is_unique_string_bit_vector(string: str) -> bool:
    # CODE HERE, no additional data structures allowed
    return True


class Test(unittest.TestCase):
    test_functions = [is_unique_string, is_unique_string_bit_vector]

    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]

    def test_string_is_unique(self):
        for test_function in self.test_functions:
            for string, expected in self.test_cases:
                assert test_function(string) == expected


if __name__ == "__main__":
    unittest.main()
