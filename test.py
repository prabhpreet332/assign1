import unittest

from Sort import sort


class TestSum(unittest.TestCase):
    def test1(self):
        """

        """
        data = [1, 2, 3]
        expected = [1, 2, 3]
        result = sort(data)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
