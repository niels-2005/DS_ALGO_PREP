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
    testable_functions = [remove_dups]
    test_cases = [
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    def test_remove_dups(self):
        for f in self.testable_functions:
            for values, expected in self.test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected


if __name__ == "__main__":
    unittest.main()
