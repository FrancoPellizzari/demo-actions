import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividirExitoso(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-8, 2), -4)
        self.assertEqual(dividir(-20, -5), 4)

    def test_dividirCero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()