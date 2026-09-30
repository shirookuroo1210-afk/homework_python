nominal = int(input("masukkan nominal uang: "))
daftar_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000,500,200,100]

for pecahan in daftar_pecahan:
    if nominal >=pecahan:
        jumlah = nominal // pecahan
        nominal = nominal % pecahan
        print(f"{jumlah} = uang {pecahan}" )
        #code written by lyvo
