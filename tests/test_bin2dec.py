# test_bin2dec.py
import unittest

# Importamos la función que queremos probar
from src.binary_conversions import convert_binary_to_decimal


class TestBin2Dec(unittest.TestCase):

    # Caso exitoso estándar
    def test_basic_conversion(self):
        # 1010 en binario es 10 en decimal
        self.assertEqual(convert_binary_to_decimal("1010"), 10)
        
    # Caso límite superior (8 bits)
    def test_maximum_length(self):
        # 11111111 es 255
        self.assertEqual(convert_binary_to_decimal("11111111"), 255)

    # Caso con un solo dígito
    def test_single_digit(self):
        self.assertEqual(convert_binary_to_decimal("0"), 0)
        self.assertEqual(convert_binary_to_decimal("1"), 1)

    # Prueba de error: Más de 8 caracteres
    def test_error_length_greater_than_eight(self):
        with self.assertRaises(ValueError):
            convert_binary_to_decimal("111111111") # 9 dígitos

    # Prueba de error: Caracteres no binarios
    def test_error_invalid_characters(self):
        with self.assertRaises(ValueError):
            convert_binary_to_decimal("1020") # El '2' es inválido


if __name__ == "__main__":
    unittest.main()