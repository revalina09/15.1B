# menggunakan kutip tiga
print('''He said, "What's there?"''')

# menggunakan karakter escape untuk tanda kutip tunggal 
print('He said, "What\'s there?"')

# menggunakan karakter escape untuk tanda kutip ganda
print("He said, \"What's there?\"")



print("ini adalah baris pertama\nDan ini baris dua")
print("ini adalah \x48\x45\x58")


print("This is \x61 \ngood example")
print(r"this is \x61 \ngood example")



#menggunakan posisi default
default_order = "{}, {} dan {}".format("Budi", "Galih","Ratna")
print('\n--- Urutan default ---')
print(default_order)

# menggunakan argument posisi
positional_order = "{1}, {0} dan {2}".format("Budi", "Galih","Ratna")
print('\n---- Urutan berdasarkan posisi ---')
print(positional_order)


# format integer
print("{0} bila duibah jadi biner menjadi {0:b}".format(12))

# format eksponensial
print("Format eksponensial: {0:e}".format(1566.345))

# pembulatan 
print("sepertiga sama dengan: {0:.3f}".format(1/3))

# Meratakan string
print("|{:<10}|{:^10}|{:.10}|".format('beras', 'gula', 'garam'))
