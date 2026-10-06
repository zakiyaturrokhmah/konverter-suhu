import unittest
from konverter_suhu import (
    celsius_ke_fahrenheit, fahrenheit_ke_celsius,
    celsius_ke_kelvin, kelvin_ke_celsius, baca_angka,
)


class TestKonverterSuhu(unittest.TestCase):
    # Test normal (seharusnya lolos)
    def test_titik_beku_air(self):
        self.assertAlmostEqual(celsius_ke_fahrenheit(0), 32)

    def test_celsius_ke_kelvin_normal(self):
        self.assertAlmostEqual(celsius_ke_kelvin(25), 298.15)

    def test_kelvin_ke_celsius_normal(self):
        self.assertAlmostEqual(kelvin_ke_celsius(273.15), 0)

    # Pencari fault
    def test_F1_fahrenheit_ke_celsius_titik_didih(self):
        """212 F harus 100 C"""
        self.assertAlmostEqual(fahrenheit_ke_celsius(212), 100, places=2)

    def test_F1_fahrenheit_ke_celsius_titik_beku(self):
        """32 F harus 0 C"""
        self.assertAlmostEqual(fahrenheit_ke_celsius(32), 0, places=2)

    def test_F2_di_bawah_nol_mutlak(self):
        """-300 C tidak mungkin ada (nol mutlak = -273.15 C)"""
        with self.assertRaises(ValueError):
            celsius_ke_kelvin(-300)

    def test_F3_input_bukan_angka(self):
        """Input 'abc' tidak boleh membuat program crash"""
        try:
            hasil = baca_angka("abc")
        except ValueError:
            self.fail("Program crash (ValueError) saat input bukan angka")
        self.assertIsNone(hasil)

    def test_F4_suhu_tubuh_presisi(self):
        """36.6 C = 97.88 F (tidak boleh dibulatkan/dipotong jadi 97)"""
        self.assertAlmostEqual(celsius_ke_fahrenheit(36.6), 97.88, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
