import unittest
from helper import *

class TestFindPair(unittest.TestCase):

	gift_card = 2500
	item_list = []

	def test_empty(self):
		self.item_list = []		
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_pair, args)

	def test_one_item(self):
		self.item_list = [('apple', 2500)]		
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_pair, args)		
			

	def test_two_items_success(self):
		self.item_list = [('apple', 0), 
						  ('banana', 2500)]		
		solution = (('apple', 0), ('banana', 2500))
		self.assertTrue(find_pair(self.item_list, self.gift_card) == solution)

	def test_two_items_fail(self):
		self.item_list = [('apple', 1000), 
					      ('banana', 1600)]
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_pair, args)

	def test_mult_items_success(self):
		self.item_list = [('apple', 400), 
					      ('banana', 900),
					      ('candy', 1600),
					      ('drakes new album', 2000)]
		solution = (('banana', 900), ('candy', 1600))
		self.assertTrue(find_pair(self.item_list, self.gift_card) == solution)

	def test_mult_items_fail(self):
		self.item_list = [('apple', 400), 
					      ('banana', 2200),
					      ('candy', 2300),
					      ('drakes new album', 4000)]
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_pair, args)

class TestFindTriple(unittest.TestCase):

	gift_card = 2500
	item_list = []

	def test_empty(self):
		self.item_list = []		
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_triple, args)

	def test_one_item(self):
		self.item_list = [('apple', 2500)]		
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_triple, args)		
			
	def test_two_items(self):
		self.item_list = [('apple', 500),
						  ('banana', 2000)]		
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_triple, args)				

	def test_three_items_success(self):
		self.item_list = [('apple', 400), 
					      ('banana', 900),
					      ('candy', 1000)]
		solution = (('apple', 400), ('banana', 900), ('candy', 1000))
		self.assertTrue(find_triple(self.item_list, self.gift_card) == solution)

	def test_three_items_fail(self):
		self.item_list = [('apple', 400), 
					      ('banana', 2200),
					      ('candy', 2300)]
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_triple, args)

	def test_mult_items_success(self):
		self.item_list = [('apple', 400), 
					      ('banana', 900),
					      ('candy', 1000),
					      ('drakes new album', 2000)]
		solution = (('apple', 400), ('banana', 900), ('candy', 1000))
		self.assertTrue(find_triple(self.item_list, self.gift_card) == solution)

	def test_mult_items_fail(self):
		self.item_list = [('apple', 400), 
					      ('banana', 2200),
					      ('candy', 2300),
					      ('drakes new album', 4000)]
		args = [self.item_list, self.gift_card]
		self.assertRaises(Exception, find_triple, args)

if __name__ == '__main__':
	unittest.main()