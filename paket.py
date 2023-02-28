from pkg.modul1 import *
from pkg.modul2 import *
from pkg.hitungnilai import hitung_nilai, kali_nilai


def main():
    # memanggil fungsi fungsi dalam modul1
    f1()
    f2()
    # memanggil fungsi fungsi dalam modul2
    f3()
    f4()


main()
print(f"\nNilai Akhir Adalah : {hitung_nilai(10, 10)}",)  # Modul Penjumlahan
print(f"Nilai Tugas Dan Nilai Tambahan : {kali_nilai(10, 10)}")  # Modul Perkalian
