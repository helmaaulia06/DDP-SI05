#soal no2 
pilih = int(input("""selamat datang diaplikasi menghitung
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
    
masukan pilihan anda: \n""")) 

match pilih:
    case 1 :
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi: "))
        luaspsg = sisi*sisi
        print("luas persegi yang sisinya",sisi, "adalah", luaspsg )
    case 2 :
        print("kamu memilih 2 untuk menghitung lingkaran")
        jari2 = int(input("masukan jari-jari: "))
        luaslkr = 3.14 * jari2 * jari2
        print("luas lingkaran yang jari-jarinya ", jari2, "adalah", luaslkr)
    case 3 :
        print("kamu memilih 3 untuk menghitung segitiga")
        alas = int(input("masukan alas segitiga: "))
        tinggi = int(input("masukan tinggi segitiga: ")) 
        luasSegitiga = 0.5 * alas * tinggi
        print("luas segitiga dengan alas ", alas, "dan tinggi", tinggi, "adalah, luasSegitiga")
    case _:
        print("anda salah pilih")
#soal no1
print("============")
#list utama :kendaraan
kendaraan = ["chery", "mobil", "1498cc", "silver", "roda 4"]

#mencetak isi dari list kendaraan
print(kendaraan)
#proses append 1 (harga kendaraan)
kendaraan.append("409.000.000.00")

#proses append 2 (tipe kendaraan)
kendaraan.append("matic")

#cetak nilai kendaraan setelah perubahan
print(kendaraan)

#sisipkan nilai untuk tipe kendaraan
kendaraan.insert(4,"Chery Automobile Co., Ltd")

#cetak hasil list akhirnya
print(kendaraan)