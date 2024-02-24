"""
untuk mendeklarasikan variable yaitu diawali dengan alphabet
dan menulisnya dengan snake case

ex : snake_case
"""

name = 'jojo'
age = 20
happy = True

print(name)
print(age)
print(happy)
print('my name %s and my age %d, ar u happy : %r' % (name, age, happy))
# %s = format string
# %d = format number
# %r = format boolean

# contoh snake case pada variable
money_bank = 2000
money_wallet = 1000

# banyak variable dalam 1 baris
name, age, born = 'joja', 30, 'august'
print(f"{name} {age} {born}")

