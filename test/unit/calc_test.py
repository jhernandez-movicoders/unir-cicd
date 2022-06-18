import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(6, self.calc.multiply(3, 2))
        self.assertEqual(0, self.calc.multiply(0, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_pow_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.pow(2, 2))
        self.assertEqual(27, self.calc.pow(3, 3))
        self.assertEqual(1, self.calc.pow(3, 0))
        self.assertEqual(0.1111111111111111, self.calc.pow(3, -2))
        self.assertEqual(3, self.calc.pow(3, 1))

    def test_pow_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.pow, "2", 2)
        self.assertRaises(TypeError, self.calc.pow, 2, "2")
        self.assertRaises(TypeError, self.calc.pow, "2", "2")
        self.assertRaises(TypeError, self.calc.pow, None, 2)
        self.assertRaises(TypeError, self.calc.pow, 2, None)
        self.assertRaises(TypeError, self.calc.pow, object(), 2)
        self.assertRaises(TypeError, self.calc.pow, 2, object())

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(9, self.calc.sqrt(81))
        self.assertEqual(0, self.calc.sqrt(0))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_sqrt_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, -2)
        self.assertRaises(TypeError, self.calc.sqrt, -4)

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        
    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())
    
    def test_log10_method_fails_with_zero_or_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -2)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
