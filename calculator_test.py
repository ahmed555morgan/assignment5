import unittest

# This is the class we want to test. So, we need to import it
import Calculator as CalculatorClass

class Test(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result = self.calculator.add(4,8)
        self.assertEqual(result,12)
    def test_0_subtract(self):
        result = self.calculator.subtract(8,4)
        self.assertEqual(result,4)
    def test_0_multiply(self):
        result = self.calculator.multiply(4,4)
        self.assertEqual(result,16)
    def test_0_power(self):
        result = self.calculator.power(2,3)
        self.assertEqual(result,8)
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()