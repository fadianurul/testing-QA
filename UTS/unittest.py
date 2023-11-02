import unittest

# Fungsi untuk menghitung faktorial


def factorial(n):
    if n < 0:
        raise ValueError("Bilangan negatif tidak memiliki faktorial")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Unit Test


class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)


if __name__ == '__main__':
    unittest.main()
