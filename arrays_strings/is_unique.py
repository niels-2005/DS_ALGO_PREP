import unittest
import time

# Question:
# Is Unique: Implement an algorithm to determine if a string has all unique characters.


def is_unique_string(string: str) -> bool:
     # CODE HERE
     return True
     


class Test(unittest.TestCase):
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
            for string, expected in self.test_cases:
                assert is_unique_string(string) == expected


if __name__ == "__main__":
    unittest.main()