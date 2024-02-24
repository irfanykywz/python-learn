"""
type data list sangat berguna karena akan banyak digunakan untuk
mengolah data secara sementara didalam program

berikut bagaimana penggunaan type data list lebih dalam
"""

data = ['one', 'two', 'three']

# menambah
data.append('four')
print(data)

# menyiispkan sebelum index tertentu
data.insert(1 , 'before-two')
print(data)

# mengetahui index dari sebuah value
print(data.index('before-two'))

# jumlah list
print(f"jumlah list: {len(data)}")

# mencari jumlah nilai yang ada dalam sebuah list
print(f"jumlah list: {data.count('one')}")

# menghapus dengan index
data.pop(1)
print(data)

# menghapus dengan value
data.remove('three')
print(data)

# menghapus dengan index range
waduh = ['w', 'a', 'd', 'u', 'h']
del waduh[0:2] # akan menghapus index 0 sampai 1
print(waduh)

# mengosongkan list
waduh = [] # reset variable menjadi kosong
print(waduh)
# cara lainnya
# print(waduh.clear())
# print(del waduh[:])

# mengcopy list agar datanya bisa dimanipulasi tanpa merusak list aslinya
chop = ['a', 'b', 'c', 'd']
docop = chop.copy()
# docop = chop[:]
docop.append('e')
print(chop)
print(docop)

# mengurutkan terbalik
rev = [1, 2, 3, 4, 5]
rev.reverse()
print(rev)

# mengurutkan
sor = [5, 4 ,3, 2, 1]
sor.sort()
print(sor)