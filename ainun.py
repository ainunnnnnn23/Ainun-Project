while True:
    user = input('\nMasukkan Nama: ')
    Nim = int(input("NIM: "))
    Kelas = input("Kelas: ")
    print(f"Hallo {user}, ")

    Harga = int(input("Masukkan Harga Barang: "))
    Barang = int(input("Jumlah Barang: "))
    Total = Harga * Barang 
    print(f"Total Harga Barang: {Total}")

    if Total > 250000:
        diskon = Total * 0.25
        total_setelah_diskon = Total - diskon
        print(f"Selamat {user}, Anda Mendapatkan Diskon 25%")
    else:
        diskon = 0
        total_setelah_diskon = Total
        print(f"Maaf {user}, Anda belum Mendapatkan Diskon")

    print(f"Total Harga yang harus dibayar: {total_setelah_diskon}")

    Ulang = input(f"Apakah {user} ingin menghitung total harga lagi? (y/n): ") 
    if Ulang != 'y':
        break

