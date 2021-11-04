import unittest

from Sort.sort import sort


class TestSort(unittest.TestCase):
    def test_sorted_list(self):
        """
        Test for sorted list
        """
        data = [1, 2, 3]
        expected = [1, 2, 3]
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test_single_element_list(self):
        """
        Test for single element list
        """
        data = [1]
        expected = [1]
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test_empty_list(self):
        """
        Test for empty list
        """
        data = []
        expected = []
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test_unsorted_list(self):
        """
        Test for unsorted list
        """
        data = [10, 2, 5, -2, 4]
        expected = [-2, 2, 4, 5, 10]
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
