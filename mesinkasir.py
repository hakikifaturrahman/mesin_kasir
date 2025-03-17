def makanan():
    global total_makan, nama_makanan
    
    total_makan = 0
    nama_makanan = []
    
    print("|================================|")
    print("|      Program Mesin Kasir       |")
    print("|================================|")
    
    while True:
        print("|        Pilih Menu Makanan      |")
        print("|================================|")
        print("| 1. Nasi Goreng    Rp.12000     |")
        print("| 2. Ayam Geprek    Rp.12000     |")
        print("| 3. Mie Goreng/Rebus Rp.5000    |")
        print("| 4. Ketoprak       Rp.7000      |")
        print("| 5. Ikan Bakar     Rp.20000     |")
        print("| 0. Selesai                     |")
        print("|================================|")
        
        menu_makanan = int(input("Pilih Menu (1/2/3/4/5/0): "))
        if menu_makanan == 0:
            break
        jumlah_porsi = int(input("Berapa Porsi: "))
        
        if menu_makanan == 1:
            total_makan += jumlah_porsi * 12000
            nama_makanan.append(("Nasi Goreng", jumlah_porsi))
        elif menu_makanan == 2:
            total_makan += jumlah_porsi * 12000
            nama_makanan.append(("Ayam Geprek", jumlah_porsi))
        elif menu_makanan == 3:
            total_makan += jumlah_porsi * 5000
            nama_makanan.append(("Mie Goreng/Rebus", jumlah_porsi))
        elif menu_makanan == 4:
            total_makan += jumlah_porsi * 7000
            nama_makanan.append(("Ketoprak", jumlah_porsi))
        elif menu_makanan == 5:
            total_makan += jumlah_porsi * 20000
            nama_makanan.append(("Ikan Bakar", jumlah_porsi))
        else:
            print("Pilihan Tidak Tersedia")

def minuman():
    global total_minum, nama_minuman
    
    total_minum = 0
    nama_minuman = []
    
    while True:
        print("|================================|")
        print("|        Pilih Menu Minuman      |")
        print("|================================|")
        print("| 1. Es Teh          Rp.4000     |")
        print("| 2. Es Jeruk        Rp.4000     |")
        print("| 3. Soda Gembira    Rp.5000     |")
        print("| 4. Kopi Susu       Rp.5000     |")
        print("| 0. Selesai                     |")
        print("|================================|")
        
        menu_minuman = int(input("Pilih Menu (1/2/3/4/0): "))
        if menu_minuman == 0:
            break
        jumlah_gelas = int(input("Berapa Gelas: "))
        
        if menu_minuman == 1:
            total_minum += jumlah_gelas * 4000
            nama_minuman.append(("Es Teh", jumlah_gelas))
        elif menu_minuman == 2:
            total_minum += jumlah_gelas * 4000
            nama_minuman.append(("Es Jeruk", jumlah_gelas))
        elif menu_minuman == 3:
            total_minum += jumlah_gelas * 5000
            nama_minuman.append(("Soda Gembira", jumlah_gelas))
        elif menu_minuman == 4:
            total_minum += jumlah_gelas * 5000
            nama_minuman.append(("Kopi Susu", jumlah_gelas))
        else:
            print("Pilihan Tidak Tersedia")

# Memanggil fungsi makanan dan minuman
makanan()
minuman()

# Menghitung total pembayaran
jumlah_semuanya = total_makan + total_minum

# Menampilkan daftar pembelian
print("|======================================================|")
print("|                    Daftar Pembelian                  |")
print("|======================================================|")

for item, jumlah in nama_makanan:
    print(f"| Nama Makanan  : {item:<33}    |")
    print(f"| Porsi         : {jumlah:<33}    |")
    print("|======================================================|")

for item, jumlah in nama_minuman:
    print(f"| Nama Minuman  : {item:<33}    |")
    print(f"| Gelas         : {jumlah:<33}    |")
    print("|======================================================|")

print("|                 Total yang harus dibayar             |")
print("|======================================================|")
print(f"| Total Harga   : Rp. {jumlah_semuanya:>10,.3f}                       |")
print("|======================================================|")