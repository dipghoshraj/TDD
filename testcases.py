import unittest
from addition import add


class TestAddFunction(unittest.TestCase):
    def test_empty_string_input(self):
        self.assertEqual(add(""), 0)

    def test_single_number_input(self):
        self.assertEqual(add("1"), 1)

    def test_multiple_numbers_input(self):
        self.assertEqual(add("1,5"), 6)

    def test_newline_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers_input(self):
        with self.assertRaises(ValueError) as context:
            add("-1,2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1, -3")

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("2,1001,6"), 8)


if __name__ == '__main__':
    unittest.main()
