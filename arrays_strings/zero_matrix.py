import unittest 
from copy import deepcopy

# Question:
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.


def zero_matrix(matrix):
    return True 


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.test_cases:
            test_matrix = deepcopy(test_matrix)
            assert zero_matrix(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()