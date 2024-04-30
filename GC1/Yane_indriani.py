print('''
      =========================================
      Graded Challenge 1
      Nama  : Yane Indriani
      Batch : RMT-031
      Program ini dibuat untuk menambah, menghapus, menampilkan barang, serta melihat total belanjaan.
      =========================================\n'''
      )

#class cartitem():
    #def objek(self, nama, *harga):
        #self.nama = nama
        #self.harga = harga5


data = []
tot_harga = []

#fungsi untuk menu 1
def input_barang():
        nama = str(input("Masukkan nama barang: "))
        harga = input("Masukkan harga:")
        data.append([nama, harga])
        print(f"Barang {nama} berhasil dimasukkan ke keranjang")
        lanjut = input('Lanjut menambahkan barang? (y/n): ')
        if lanjut == 'y':
            input_barang()
        

#fungsi untuk menu 2
def hapus_barang():
    hapus_barang = input("Masukkan nama barang yang ingin di hapus: ")
    if hapus_barang in data:
        data.remove(hapus_barang)
        lanjut = input("Lanjut menghapus: (y/n)")
        if lanjut == 'y':
            hapus_barang()
    else:
        print("Barang tidak ditemukan")

def tampil_barang():
    if len(data) == 0:
        print("Tidak ada barang di keranjang")
    else:
        print("Barang di keranjang:\n")
        for i, item in enumerate(data):
            print(f"{i+1} | {item[0]} - {item[1]}")
        print()

def total_belanja():
    a = 0
    for i in tot_harga:
        total = a + i 
    print("Total belanja: Rp.", total)

while True:
    print('''
            ===================================================
            Selamat Datang di Keranjang Belanja di Toko Makmur!
            ===================================================
            ''')
    print("Menu: ")
    print("1. Menambah Barang: ")
    print("2. Hapus Barang: ")
    print("3. Tampilkan Barang di Keranjang: ")
    print("4. Lihat Total Belanja: ")
    print("5. Exit")

    pilihan = input("\n Pilihan: ")

    if pilihan.lower() == '5':
        print("Sampai jumpa!Terima kasih sudah belanja di Toko Makmur")
        break
    elif pilihan == '1':
        input_barang()
    elif pilihan == '2':
        hapus_barang()
    elif pilihan == '3':
        tampil_barang()
    elif pilihan == '4':
        total_belanja()
    else:
        print("Pilihannya salah. Coba lagi ya.\n")