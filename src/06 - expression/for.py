
setups = [
    'mouse',
    'keyboard',
    'laptop',
    'bag',
    'modem',
    'charger'
]

# penggunaan for untuk membaca list
for read in setups:
    print(read)

# penggunaan for untuk perluangan dari jumlah data
for index in range(len(setups)):
    print(setups[index])

# pengunaan for dalam jangkauan angka
for i in range(5):
    print(i)

# perulangan bintang
max = 5
for i in range(max):
    for j in range(0, max - 1):
        print("*", end=" ")
    print()
    max = max-1

# perulangan index dan data
for index, data in enumerate(setups):
    print(f"index {index} data : {data}")

# perulangan nested list
nes_data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]
for red in nes_data:
    for dat in red:
        print(dat, end=" ")
    print()