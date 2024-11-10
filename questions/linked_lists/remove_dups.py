import unittest

from linked_list import LinkedList

# Question:
# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?


def remove_dups(ll: LinkedList) -> LinkedList:
    return True


def remove_dups_followup(ll: LinkedList) -> LinkedList:
    return True


class Test(unittest.TestCase):
    testable_functions = [remove_dups, remove_dups_followup]
    test_cases = [
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    def test_remove_dups(self):
        for test_function in self.testable_functions:
            for input_ll, expected_ll in self.test_cases:
                assert test_function(input_ll) == expected_ll


if __name__ == "__main__":
    unittest.main()
