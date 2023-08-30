#!/usr/bin/env python3
from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nestedMap, path, expectedResult):
        """
        Test the access_nested_map function with different input scenarios.

        Args:
            nestedMap (dict): The nested map to be accessed.
            path (tuple): The path to the desired value within the nested map.
            expectedResult: The expected result when accessing the nested map.
        """
        self.assertEqual(access_nested_map(nestedMap, path), expectedResult)


if __name__ == '__main__':
    unittest.main()
