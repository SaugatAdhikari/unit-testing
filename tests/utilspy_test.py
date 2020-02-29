import os
import unittest

class Testutils(unittest.TestCase):
    def test_add_numbers(self):
        num1 = "10"
        num2 = 5

        #assert that the datatype of both num1 and num2 is integer
        self.assertIsInstance(num1, int)
        self.assertIsInstance(num2, int)
    
    def test_list_length(self):
        list1 = [1,2,3]
        list2 = [1,2,3,4]
        list3 = [3,4,5,6]
        
        #assert that the length of the lists are equal
        self.assertEqual(len(list1), len(list2))
        self.assertEqual(len(list2), len(list3))

if __name__ == '__main__':
    unittest.main()