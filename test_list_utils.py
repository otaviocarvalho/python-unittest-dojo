import unittest
import list_utils 

class TestSumList(unittest.TestCase):
    def test_sum_with_a_single_number(self):
        list_with_a_single_number = [1]
        sum_result = list_utils.sum(list_with_a_single_number) 
        self.assertEqual(sum_result, 1, "Sum of a single number should be 1")

    def test_sum_with_a_multiple_numbers(self):
        list_with_multiple_numbers = [1,2,3]
        sum_result = list_utils.sum(list_with_multiple_numbers) 
        self.assertEqual(sum_result, 6, "Sum of multiple numbers should be 6")

if __name__ == '__main__':
    unittest.main()