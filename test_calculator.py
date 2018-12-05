import unittest
import calculator 

class TestCalculator(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(calculator.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(calculator.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()