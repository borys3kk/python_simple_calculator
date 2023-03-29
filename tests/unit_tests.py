import sys
from math import sqrt
import unittest
sys.path.append('../calculator')
from calculator import Calculator
from apihandler import ApiHandler
from calculatorgui import CalculatorGUI

class TestApi(unittest.TestCase):
    def setUp(self):
        self.api_handler = ApiHandler()

    def test_change_func(self):
        functions = ['sinx', 'x^5-2x^3+1', '1/x']
        for func in functions:
            self.api_handler.set_new_func_param(func)
            self.assertEqual(func, self.api_handler.params['input'])

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.calculator_gui = CalculatorGUI()
        self.calculator_gui.open_main_window()
    
    def test_remove_char(self):
        self.calculator_gui.set_display_data('1234')
        self.calculator_gui.remove_char()
        self.assertEqual('123', self.calculator_gui.get_display_data())
        
        self.calculator_gui.set_display_data('1234')
        self.calculator_gui.change_sign()
        self.assertEqual('-1234', self.calculator_gui.get_display_data())
        self.calculator_gui.change_sign()
        self.assertEqual('1234', self.calculator_gui.get_display_data())

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.reset()
   
    def test_add(self):
        self.calculator.set_first('2137')
        self.calculator.set_second('1269')
        self.calculator.set_operation('+')
        self.calculator.handle_operations()
        self.assertEqual(str(float(2137 + 1269)), self.calculator.get_result())

    def test_subtract(self):
        self.calculator.set_first('2137')
        self.calculator.set_second('1269')
        self.calculator.set_operation('-')
        self.calculator.handle_operations()
        self.assertEqual(str(float(2137 - 1269)), self.calculator.get_result())
    
    def test_multiply(self):
        self.calculator.set_first('2137')
        self.calculator.set_second('1269')
        self.calculator.set_operation('*')
        self.calculator.handle_operations()
        self.assertEqual(str(float(2137 * 1269)), self.calculator.get_result())
    
    def test_divide(self):
        self.calculator.set_first('2137')
        self.calculator.set_second('1269')
        self.calculator.set_operation('/')
        self.calculator.handle_operations()
        self.assertEqual(str(float(2137 / 1269)), self.calculator.get_result())
    
    def test_exponenta(self):
        self.calculator.set_first('23')
        self.calculator.set_second('12')
        self.calculator.set_operation('^')
        self.calculator.handle_operations()
        self.assertEqual(str(float(23 ** 12)), self.calculator.get_result())

    def test_sqrt(self):
        self.calculator.set_first('81')
        self.calculator.sqrt()
        self.assertEqual(str(float(sqrt(81))), self.calculator.get_result())
    

if __name__ == '__main__':
    unittest.main()