
USERNAME = "el"
PASS = "123"
percobaan = 3

while percobaan > 0:
    input_user = input("Masukkan username: ")
    input_pass = input("Masukkan password: ")

    if input_user == USERNAME and input_pass == PASS:
        print("\nSelamat datang di aplikasi Gesit Pasti Sampai.")
        print("Pilih Menu:")
        print("1. Biaya Ongkir")
        print("2. Data Inventaris")

        pilih_menu = int(input("Silakan pilih menu 1 atau 2: "))

        if pilih_menu == 1:
            banyak_paket = int(input("Berapa banyak paket yang akan dikirim: "))
            tujuan_paket = int(input("Tujuan pengiriman dalam kota (1) / luar kota (2): "))

            total_ongkir = 0

            if tujuan_paket == 1 or tujuan_paket == 2:

                for i in range(banyak_paket):
                    berat_paket = int(input(f"Berat paket {i+1} (kg): "))

                    if berat_paket <= 0:
                        print("Berat paket tidak valid!")
                        continue

                    if tujuan_paket == 1:
                        if berat_paket <= 1:
                            ongkir = berat_paket * 80000
                        elif berat_paket <= 5:
                            ongkir = berat_paket * 150000
                        elif berat_paket <= 9:
                            ongkir = berat_paket * 25000
                        else:
                            ongkir = berat_paket * 40000

                    elif tujuan_paket == 2:
                        if berat_paket <= 1:
                            ongkir = berat_paket * 15000
                        elif berat_paket <= 5:
                            ongkir = berat_paket * 30000
                        elif berat_paket <= 9:
                            ongkir = berat_paket * 50000
                        else:
                            ongkir = berat_paket * 80000

                    total_ongkir += ongkir

                if tujuan_paket == 1:
                    print(f"\nTotal biaya pengiriman {banyak_paket} paket dalam kota adalah Rp{total_ongkir:,}")
                else:
                    print(f"\nTotal biaya pengiriman {banyak_paket} paket luar kota adalah Rp{total_ongkir:,}")

                print("Terima kasih telah menggunakan Gesit Pasti Sampai.")

            else:
                print("Tujuan pengiriman tidak valid!")

        elif pilih_menu == 2:
            inventaris = {
                "BRG001": ["Dus", 25],
                "BRG002": ["Lakban", 10],
                "BRG003": ["Kertas", 30],
                "BRG004": ["Spidol", 4]
            }

            print("\n===== Data Inventaris =====")
            input_kode = input("Masukkan kode barang: ")

            if input_kode in inventaris:
                print(f"Nama barang: {inventaris[input_kode][0]}")
                print(f"Jumlah stok: {inventaris[input_kode][1]}")
            else:
                print("Kode barang tidak ditemukan!")

        else:
            print("Pilihan menu tidak valid!")

        break

    else:
        percobaan -= 1

        if percobaan > 0:
            print(f"Login salah! Kesempatan Anda {percobaan}x lagi.\n")
        else:
            print("Anda tidak diperkenankan mengakses aplikasi ini.")
