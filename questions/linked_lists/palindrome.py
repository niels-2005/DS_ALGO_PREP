import unittest

from linked_list import LinkedList

# Question:

# Palindrome: Implement a function to check if a linked list is a palindrome.


def is_palindrome(ll: LinkedList):
    return True


class Test(unittest.TestCase):
    test_cases = [
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1], True),
        (["a", "a"], True),
        ("aba", True),
        ([], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2], False),
    ]

    def test_is_palindrome(self):
        for values, expected in self.test_cases:
            assert is_palindrome(LinkedList(values)) == expected


if __name__ == "__main__":
    unittest.main()
