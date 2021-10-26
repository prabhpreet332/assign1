import unittest

from Sort.sort import sort


class TestSort(unittest.TestCase):
    def test1(self):
        """
        Test for sorted list
        """
        data = [1, 2, 3]
        expected = [1, 2, 3]
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test2(self):
        """
        Test for single element list
        """
        data = [1]
        expected = [1]
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test3(self):
        """
        Test for empty list
        """
        data = []
        expected = []
        result = sort(data)
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test4(self):
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
