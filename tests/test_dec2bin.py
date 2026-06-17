# tests/test_dec2bin.py
import unittest

# Importamos la función correcta
from src.binary_conversions import convert_decimal_to_binary 

class TestDec2Bin(unittest.TestCase):

    # Caso estándar exitoso
    def test_basic_conversion(self):
        # 10 en decimal es 1010 en binario
        self.assertEqual(convert_decimal_to_binary(10), "1010")
        self.assertEqual(convert_decimal_to_binary(6), "110")
        
    # Caso límite (el cero)
    def test_zero_conversion(self):
        self.assertEqual(convert_decimal_to_binary(0), "0")

    # Caso con potencia de 2 (fáciles de verificar: un 1 seguido de ceros)
    def test_powers_of_two(self):
        self.assertEqual(convert_decimal_to_binary(1), "1")
        self.assertEqual(convert_decimal_to_binary(4), "100")
        self.assertEqual(convert_decimal_to_binary(16), "10000")

    # Caso límite superior (equivalente a tus 8 bits, máximo 255)
    def test_maximum_eight_bit_value(self):
        # 255 en decimal es 11111111 en binario
        self.assertEqual(convert_decimal_to_binary(255), "11111111")


if __name__ == "__main__":
    unittest.main()