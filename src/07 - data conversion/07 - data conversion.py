"""
setiap type data bisa dikonversi keberbagai type data lainnya
"""

# string to int
nilai = "10"
print(type(nilai))
print(type(int(nilai)))

# range to list
print(list(range(0, 10)))

# string to list
print(list('heheboi'))

# tuple to list
print(list(('a', 'b', 'c')))