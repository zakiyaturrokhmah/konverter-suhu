# Konverter Suhu (Python)

Mini program konsol untuk mengonversi suhu antara Celsius, Fahrenheit, dan Kelvin.
Dibuat untuk Tugas Pertemuan 3: menemukan defect/fault dan membuat RCA.

## Menjalankan
    python konverter_suhu.py

## Menjalankan test (menemukan fault)
    python -m unittest test_konverter_suhu -v

Hasil: 8 test, 3 lolos, 5 gagal (mewakili 4 fault: F1-F4).

## Laporan test berwarna (untuk screenshot)
    python jalankan_test.py              # program asli
    python jalankan_test.py perbaikan    # versi perbaikan

## Struktur
- `jalankan_test.py` : laporan pengujian berbentuk tabel
- `konverter_suhu.py` : program (versi dengan fault)
- `test_konverter_suhu.py` : skrip test
- `perbaikan/konverter_suhu.py` : versi setelah perbaikan (semua test lolos)
