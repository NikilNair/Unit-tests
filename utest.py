import unittest

from calc import add, sub, mul, div

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum two numbers
        """
        result = add(2, 4)
        self.assertEqual(result, 6)

class TestSub(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can subtract two numbers
        """

        result = sub(2, 4)
        self.assertEqual(result, -2)

class TestMul(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can multiply two numbers
        """
        result = mul(2, 4)
        self.assertEqual(result, 8)

class TestDiv(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can divide two numbers
        """
        result = div(2, 4)
        self.assertEqual(result, 0.5)





if __name__ == '__main__':
    unittest.main()
