import unittest

from linked_list import LinkedList

# Question:
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.


def kth_to_last(ll: LinkedList, k: int):
    return True

def kth_last_recursive(ll: LinkedList, k: int):
    return True


class Test(unittest.TestCase):
    test_cases = [
        ((10, 20, 30, 40, 50), 1, 50),
        ((10, 20, 30, 40, 50), 5, 10),
    ]

    def test_kth_to_last(self):
        for input_ll, k, expected in self.test_cases:
            assert kth_to_last(input_ll, k) == expected


if __name__ == "__main__":
    unittest.main()
