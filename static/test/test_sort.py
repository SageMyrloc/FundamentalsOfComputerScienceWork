import unittest
from sort import bubble_sort
from sort import quicksort


class TestBubbleSort(unittest.TestCase):

    def test_bs_with_positive_numbers(self):
        self.assertEqual(bubble_sort([5, 5, 7, 8, 2, 4, 1]), [1, 2, 4, 5, 5, 7, 8])

    def test_bs_empty_list(self):
        self.assertEqual(bubble_sort([]), [])


# Below are the two tests i have written to go along side those above. The first ensures it sorts negative numbers, the second ensures it can deal with a mix of numbers.
    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-5, -5, -7, -8, -2, -4, -1]), [-8, -7, -5, -5, -4, -2, -1])

    def test__multinumber_array(self):
        self.assertEqual(quicksort([5, -5, 3, -3, 2, -2, 4, -4, 1, -1, 6, -6, 7, -7, 8]), [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main(verbosity=2)
