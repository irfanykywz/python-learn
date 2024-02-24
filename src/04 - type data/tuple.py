"""
perbedaan list dan tuple yaitu
list = mutable
tuple = immutable

mutable artinya data bisa diubah ubah
immutable datanya tidak bisa diubah alias tetap
"""

# tuple packing
name = 'jojo'
age = 20
profess = 'selling'

dat = (name, age, profess)
print(dat)

# tuple unpacking
xname, xage, xprofess = dat
print(f"{xname} {xage} {xprofess}")