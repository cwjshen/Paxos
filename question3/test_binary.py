import unittest
from helper import *

class TestFindPair(unittest.TestCase):
	curr_string = ""
	input_string = ""
	args = [curr_string, input_string]

	def test_empty(self):
		self.assertRaises(Exception, binary_x, self.args)

	def test_one_char_1(self):
		self.input_string = "1"
		self.assertTrue(binary_x(self.input_string, self.curr_string) == '1')

	def test_one_char_0(self):
		self.input_string = "0"
		self.assertTrue(binary_x(self.input_string, self.curr_string) == '0')		


	def test_one_char_X(self):
		self.input_string = "X"
		self.assertTrue(binary_x(self.input_string, self.curr_string) == binary_x("","0") + binary_x("","1"))	

	def test_mult_char(self):
		self.input_string = "1X1"
		self.assertTrue(binary_x(self.input_string, self.curr_string) == binary_x("X1", "1"))
			

if __name__ == '__main__':
	unittest.main()