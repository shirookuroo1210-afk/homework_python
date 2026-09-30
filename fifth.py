def tipe_karakter():
    karakter = input("masukkan teks apapun: ").lower()

    if karakter == "a" or karakter == "i" or karakter == "u" or karakter == "e" or karakter == "o":
        print("alphabet tersebut termasuk golongan vokal")
    else:
        print("alphabet tersebut termasuk golongan konsonan")

    tipe_karakter()
    pengulangan = input("apakah ingin mengulang? (y/n): ").lower()

while True:
    if pengulangan == "y":
         tipe_karakter()
         pengulangan = input("apakah ingin mengulang? (y/n): ").lower()
    else:
        print('oh ok')
        break