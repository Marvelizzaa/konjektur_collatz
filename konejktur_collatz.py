def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"


def proses_angka():
    input_angka = int(input("Masukkan angka: "))
    status = cek_ganjil_genap(input_angka)
    if status == "ganjil":
        hasil = input_angka * 3 + 1
        print(f"Angka ganjil, hasil: {hasil}")
    else:
        hasil = input_angka // 2
        print(f"Angka genap, hasil: {hasil}")
        
def main():
    while True:
        proses_angka()
        lanjut = input("Apakah anda ingin melanjutkan? (y/n): ")
        if lanjut.lower() != 'y':
            print("makasih yaaa")
            break
main()