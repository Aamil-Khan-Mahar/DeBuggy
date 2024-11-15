
import unittest
from Code8Correct.py import bubble_sort, binary_search  # Replace with the correct file name if needed

class TestSortAndSearch(unittest.TestCase):

    def test_bubble_sort(self):
        # Test case for sorting an unsorted list
        unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = bubble_sort(unsorted_arr)
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])

    def test_bubble_sort_empty(self):
        # Test case for an empty list
        empty_arr = []
        sorted_arr = bubble_sort(empty_arr)
        self.assertEqual(sorted_arr, [])

    def test_bubble_sort_single_element(self):
        # Test case for a list with a single element
        single_element_arr = [5]
        sorted_arr = bubble_sort(single_element_arr)
        self.assertEqual(sorted_arr, [5])

    def test_bubble_sort_duplicates(self):
        # Test case for a list with duplicate values
        arr_with_duplicates = [3, 1, 2, 3, 3, 1]
        sorted_arr = bubble_sort(arr_with_duplicates)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 3])

    def test_binary_search_found(self):
        # Test case for binary search where the element is found
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        index = binary_search(arr, target)
        self.assertEqual(index, 4)

    def test_binary_search_not_found(self):
        # Test case for binary search where the element is not found
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        index = binary_search(arr, target)
        self.assertEqual(index, -1)

    def test_binary_search_empty(self):
        # Test case for binary search with an empty list
        arr = []
        target = 3
        index = binary_search(arr, target)
        self.assertEqual(index, -1)

    def test_binary_search_single_element_found(self):
        # Test case for binary search with a single element (found)
        arr = [3]
        target = 3
        index = binary_search(arr, target)
        self.assertEqual(index, 0)

    def test_binary_search_single_element_not_found(self):
        # Test case for binary search with a single element (not found)
        arr = [3]
        target = 5
        index = binary_search(arr, target)
        self.assertEqual(index, -1)

if __name__ == '__main__':
    unittest.main()
