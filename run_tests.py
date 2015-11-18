# -*- coding: utf-8 -*-

import unittest
import sys

from test_calculator import CalculatorTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CalculatorTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
