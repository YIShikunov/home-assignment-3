# -*- coding: utf-8 -*-

import unittest
from calc import calculate, ERRMSG


class CalculatorTestCase(unittest.TestCase):
    
	def test_fractions_add(self):
		r = calculate("3.04+-4.04")
		self.assertEqual(r, -1.0)

	def test_fractiond_sub(self):
		r = calculate("3.04--4.06")
		self.assertEqual(r, 7.1)
		
	def test_fractons_div(self):
		r = calculate("5.6/4.3")
		self.assertEqual(r, 5.6/4.3)
	
	def test_div_negative(self):
		r = calculate("5.6/-4.3")
		self.assertEqual(r, -5.6/4.3)
		
	def test_mul_negatives(self):
		r = calculate("-4*-11")
		self.assertEqual(r, 44)
		
	def test_factor_correct(self):
		r = calculate("5!")
		self.assertEqual(r, 120)
		
	def test_factor_wrong(self):
		r = calculate("5.0!")
		self.assertEqual(r, ERRMSG)
		
	def test_div_zero(self):
		r = calculate("1.0/0.0")
		self.assertEqual(r, ERRMSG)
		
	def test_multiple_operand(self):
		r = calculate("1/2-4")
		self.assertEqual(r, ERRMSG)
		
	def test_wrong_operator(self):
		r = calculate("8.0$3")
		self.assertEqual(r, ERRMSG)
		
	def test_text(self):
		r = calculate("hello world two plus two")
		self.assertEqual(r, ERRMSG)
		
	def test_weird_line(self):
		r = calculate("\n\r\t\s")
		self.assertEqual(r, ERRMSG)
		
	def test_spaces(self):
		r = calculate("3 - 3")
		self.assertEqual(r, ERRMSG)
	
	def test_multiple_decimals(self):
		r = calculate("1.2.3-3.4.5")
		self.assertEqual(r, ERRMSG)
		