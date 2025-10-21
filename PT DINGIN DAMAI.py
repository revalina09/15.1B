# Program Perhitungan Gaji Karyawan PT. DINGIN DAMAI

# Gaji pokok
gaji_pokok = 300000

# Input Golongan
print("=== Tunjangan Jabatan ===")
print("Golongan 1 = 5%")
print("Golongan 2 = 10%")
print("Golongan 3 = 15%")
golongan = int(input("Masukkan Golongan (1/2/3): "))

# Hitung tunjangan jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid, tunjangan jabatan = 0")

# Input Pendidikan
print("\n=== Tunjangan Pendidikan ===")
print("SMA = 2.5%")
print("D1  = 5%")
print("D3  = 20%")
print("S1  = 30%")
pendidikan = input("Masukkan Pendidikan (SMA/D1/D3/S1): ").upper()

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid, tunjangan pendidikan = 0")

# Input Jam kerja
jam_kerja = int(input("\nMasukkan jumlah jam kerja hari ini: "))

# Hitung honor lembur
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Output
print("\n===== SLIP GAJI KARYAWAN =====")
print("Gaji Pokok               : Rp", gaji_pokok)
print("Tunjangan Jabatan        : Rp", int(tunjangan_jabatan))
print("Tunjangan Pendidikan     : Rp", int(tunjangan_pendidikan))
print("Honor Lembur             : Rp", lembur)
print("-------------------------------")
print("Total Gaji               : Rp", int(total_gaji))
