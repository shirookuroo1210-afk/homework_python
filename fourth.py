teks = input("masukkan teks: ")
frekuensi = {}

for huruf in teks:
    if huruf in frekuensi:
        frekuensi[huruf] +=1
    else:
        frekuensi[huruf] = 1

hasil = ""

for kunci,nilai in frekuensi.items():
    hasil = hasil + kunci + "=" + str(nilai) + ", "
print(hasil)
#code written by lyvo
