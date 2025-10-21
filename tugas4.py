# Program menghitung gaji pegawai

# Input
gp = float(input("Masukkan Gaji Pokok: "))
jk = int(input("Masukkan Total Jam Kerja: "))

# Hitung tunjangan
tjg = 0.2 * gp

# Hitung lembur
if jk > 200:
    lm = (jk - 200) * 20000
else:
    lm = 0

# Hitung gaji kotor
gaji_kotor = gp + tjg + lm

# Pajak 10%
pajak = 0.1 * gaji_kotor

# Gaji bersih
gaji_bersih = gaji_kotor - pajak

# Output
print("\n--- Gaji Pegawai ---")
print(f"Gaji Pokok     : Rp {gp:,.0f}")
print(f"Tunjangan (20%): Rp {tjg:,.0f}")
print(f"Lembur         : Rp {lm:,.0f}")
print(f"Gaji Kotor     : Rp {gaji_kotor:,.0f}")
print(f"Pajak (10%)    : Rp {pajak:,.0f}")
print(f"Gaji Bersih    : Rp {gaji_bersih:,.0f}")
