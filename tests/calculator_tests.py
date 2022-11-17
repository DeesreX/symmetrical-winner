""" Unittests for the basic calculator module."""
import unittest
from src.basic_calculator import basic_calculator

class BasicCalculatorTest(unittest.TestCase):
    """Unittests for the basic calculator module."""
    def test_basic_calculations(self):
        basic_calculations = [
            ("1+2", "3"),
            ("1-2", "-1"),
            ("1*2", "2"),
            ("1/2", "0.5"),
        ]
        
        for calculation in basic_calculations:
            calculator = basic_calculator.BasicCalculator()
            result = calculator.calculate(calculation[0])
            self.assertEqual(result, calculation[1])