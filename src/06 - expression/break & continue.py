"""
break  = untuk memberhentikan perulangan
continue = untuk melangkahi perulangan ke perulangan selanjutnya
"""

# contoh penggunaan break
while True:
    print("ini hanya akan muncul 1x")
    break

# contoh penggunaan continue
data = [1, 2, 3, 4, 5]
for num in data:
    # jika num = angka 2 maka akan dilewati dan tidak akan diprint
    if num == 2:
        continue
    print(num)