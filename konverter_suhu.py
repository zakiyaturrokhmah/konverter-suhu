"""Konverter Suhu - mini program sederhana (Celsius, Fahrenheit, Kelvin)."""


def celsius_ke_fahrenheit(c):
    return int(c * 9 / 5 + 32)


def fahrenheit_ke_celsius(f):
    return f - 32 * 5 / 9


def celsius_ke_kelvin(c):
    return c + 273.15


def kelvin_ke_celsius(k):
    return k - 273.15


def baca_angka(teks):
    return float(teks)


def tampilkan_menu():
    print("=== KONVERTER SUHU ===")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Celsius -> Kelvin")
    print("4. Kelvin -> Celsius")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Terima kasih!")
            break
        if pilihan not in {"1", "2", "3", "4"}:
            print("Menu tidak valid.\n")
            continue

        nilai = baca_angka(input("Masukkan suhu: "))

        if pilihan == "1":
            print(f"Hasil: {celsius_ke_fahrenheit(nilai)} °F\n")
        elif pilihan == "2":
            print(f"Hasil: {fahrenheit_ke_celsius(nilai):.2f} °C\n")
        elif pilihan == "3":
            print(f"Hasil: {celsius_ke_kelvin(nilai):.2f} K\n")
        elif pilihan == "4":
            print(f"Hasil: {kelvin_ke_celsius(nilai):.2f} °C\n")


if __name__ == "__main__":
    main()
