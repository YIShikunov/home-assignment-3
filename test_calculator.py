# -*- coding: utf-8 -*-

import unittest
from calc import calculate, ERROR_MESSAGE


class CalculatorTestCase(unittest.TestCase):
    
	def test_fractions_add(self):
		r = calculate("3.04+-4.04")
		self.assertEqual(r, '-1.00')

	def test_fractiond_sub(self):
		r = calculate("3.04--4.06")
		self.assertEqual(r, '7.10')
		
	def test_fractons_div(self):
		r = calculate("6.6/3.3")
		self.assertEqual(r, '2')
	
	def test_div_negative(self):
		r = calculate("6.6/-3.3")
		self.assertEqual(r, '-2')
		
	def test_mul_negatives(self):
		r = calculate("-4*-11")
		self.assertEqual(r, '44')
		
	def test_factor_correct(self):
		r = calculate("5!")
		self.assertEqual(r, 120)
		
	def test_factor_wrong(self):
		r = calculate("5.0!")
		self.assertEqual(r, ERROR_MESSAGE)
	
	def test_factor_zero(self):
		r = calculate("0!")
		self.assertEqual(r, 1)
		
	def test_div_zero(self):
		r = calculate("1.0/0.0")
		self.assertEqual(r, ERROR_MESSAGE)
		
	def test_multiple_operand(self):
		r = calculate("1/2-4")
		self.assertEqual(r, ERROR_MESSAGE)
		
	def test_wrong_operator(self):
		r = calculate("2.4$3")
		self.assertEqual(r, ERROR_MESSAGE)
		
	def test_text(self):
		r = calculate("hello world two plus two")
		self.assertEqual(r, ERROR_MESSAGE)
		
	def test_spaces(self):
		r = calculate("3 - 3")
		self.assertEqual(r, ERROR_MESSAGE)
		