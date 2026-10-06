NOL_MUTLAK_C = -273.15

def celsius_ke_fahrenheit(c):
    return c * 9 / 5 + 32          # F4: hapus int()

def fahrenheit_ke_celsius(f):
    return (f - 32) * 5 / 9        # F1: tambah kurung

def celsius_ke_kelvin(c):
    if c < NOL_MUTLAK_C:           # F2: validasi nol mutlak
        raise ValueError("Suhu di bawah nol mutlak (-273.15 C)")
    return c + 273.15

def kelvin_ke_celsius(k):
    if k < 0:
        raise ValueError("Kelvin tidak boleh negatif")
    return k - 273.15

def baca_angka(teks):
    try:                           # F3: tangani input bukan angka
        return float(teks)
    except ValueError:
        return None
