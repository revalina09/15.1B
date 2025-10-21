# input
pembeli = input("Input Nama Pembeli : ")
no_hp = input("Input No. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

# proses
if jurusan == "SBY":
    nama_jurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    nama_jurusan = "Bali"
    harga = 350000
else:
    nama_jurusan = "Lampung"
    harga = 500000

# Input Jumlah Beli
jumlah = int(input("Masukan Jumlah Beli : "))

# proses potongan
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0

total = (jumlah * harga) - potongan

# cetak hasil
print("-------------------")
print("       PENJUALAN TIKET BUS        ")
print("             XYZ                   ")
print("-------------------")
print("Nama Pembeli        : ", pembeli)
print("No Handphone        : ", no_hp)
print("Kode Jurusan        : ", jurusan)
print("Nama Kota Tujuan    : ", nama_jurusan)
print("Harga               : ", harga)
print("Jumlah Beli         : ", jumlah)
print("-----------------------------------")
print("Potongan            : ", potongan)
print("Total Bayar         : ", total)

ubay = int(input("Masukan Uang Bayar : "))
uang_kembali = ubay - total
print("Uang Kembali        : ", uang_kembali)
