"""Laporan pengujian Konverter Suhu (tabel berwarna, siap di-screenshot).

Cara pakai:
    python jalankan_test.py              -> uji program asli
    python jalankan_test.py perbaikan    -> uji versi perbaikan
"""
import os
import sys
import importlib.util

os.system("")  # mengaktifkan warna ANSI di terminal Windows
HIJAU, MERAH, KUNING, BIRU, ABU, TEBAL, RESET = (
    "\033[92m", "\033[91m", "\033[93m", "\033[96m", "\033[90m", "\033[1m", "\033[0m")

folder = sys.argv[1] if len(sys.argv) > 1 else "."
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder, "konverter_suhu.py")
spec = importlib.util.spec_from_file_location("konverter_suhu", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def angka(func, args, harapan, satuan, tol=0.01):
    try:
        a = func(*args)
    except Exception as e:
        return f"ERROR {type(e).__name__}", False
    return f"{a:.2f} {satuan}".replace(".00 ", " "), abs(a - harapan) <= tol


def harus_error(func, args):
    try:
        a = func(*args)
    except ValueError:
        return "ValueError (ditolak)", True
    return f"{a:.2f} K (diterima)", False


def input_aneh(teks):
    try:
        a = m.baca_angka(teks)
    except Exception as e:
        return f"CRASH {type(e).__name__}", False
    return ("None (ditangani)", True) if a is None else (str(a), False)


# (ID test, fault, skenario, input, diharapkan, fungsi pengetes)
KASUS = [
    ("TC01", "-",  "Titik beku air C->F",     "0 C",     "32 F",     lambda: angka(m.celsius_ke_fahrenheit, (0,), 32, "F")),
    ("TC02", "-",  "Celsius ke Kelvin",       "25 C",    "298.15 K", lambda: angka(m.celsius_ke_kelvin, (25,), 298.15, "K")),
    ("TC03", "-",  "Kelvin ke Celsius",       "273.15 K", "0 C",     lambda: angka(m.kelvin_ke_celsius, (273.15,), 0, "C")),
    ("TC04", "F1", "Titik didih air F->C",    "212 F",   "100 C",    lambda: angka(m.fahrenheit_ke_celsius, (212,), 100, "C")),
    ("TC05", "F1", "Titik beku air F->C",     "32 F",    "0 C",      lambda: angka(m.fahrenheit_ke_celsius, (32,), 0, "C")),
    ("TC06", "F2", "Di bawah nol mutlak",     "-300 C",  "ValueError", lambda: harus_error(m.celsius_ke_kelvin, (-300,))),
    ("TC07", "F3", "Input bukan angka",       "'abc'",   "None",     lambda: input_aneh("abc")),
    ("TC08", "F4", "Presisi suhu tubuh C->F", "36.6 C",  "97.88 F",  lambda: angka(m.celsius_ke_fahrenheit, (36.6,), 97.88, "F")),
]

LEBAR = [5, 5, 25, 10, 12, 22, 6]
KEPALA = ["ID", "Fault", "Skenario", "Input", "Diharapkan", "Aktual", "Status"]
garis = "+" + "+".join("-" * (w + 2) for w in LEBAR) + "+"


def baris(sel, warna=None):
    out = "|" + "|".join(f" {str(s)[:w].ljust(w)} " for s, w in zip(sel, LEBAR)) + "|"
    return f"{warna}{out}{RESET}" if warna else out


nama = "VERSI PERBAIKAN" if folder != "." else "PROGRAM ASLI"
print(f"\n{TEBAL}{BIRU}  LAPORAN PENGUJIAN - KONVERTER SUHU ({nama}){RESET}")
print(f"{ABU}  Framework: Python | Metode: black-box, boundary value, negative testing{RESET}\n")
print(garis)
print(baris(KEPALA, TEBAL))
print(garis)

lulus = gagal = 0
fault_gagal = set()
for id_, fault, skenario, inp, harap, uji in KASUS:
    aktual, ok = uji()
    status = "PASS" if ok else "FAIL"
    lulus, gagal = lulus + ok, gagal + (not ok)
    if not ok:
        fault_gagal.add(fault)
    print(baris([id_, fault, skenario, inp, harap, aktual, status], HIJAU if ok else MERAH))
print(garis)

total = lulus + gagal
print(f"\n  Total test : {total}")
print(f"  {HIJAU}Lulus      : {lulus}{RESET}")
print(f"  {MERAH}Gagal      : {gagal}{RESET}")
if fault_gagal:
    print(f"  {KUNING}Fault terdeteksi: {', '.join(sorted(fault_gagal))} ({len(fault_gagal)} fault){RESET}")
    print(f"\n  {MERAH}{TEBAL}HASIL: ADA FAULT{RESET}\n")
else:
    print(f"\n  {HIJAU}{TEBAL}HASIL: SEMUA TEST LULUS{RESET}\n")
