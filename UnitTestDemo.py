'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
import unittest
import sys
sys.path.append("F:/AllState_Python2018")
from finance import addTax

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( addTax(46985,2), 47567.700000000004)
 
    
 
if __name__ == '__main__':
    unittest.main()
