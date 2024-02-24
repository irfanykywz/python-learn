from program import wow


"""
ketika memanggil module dari file program.py
maka kode yang ada didalam __name__ == '__main__'
tidak akan dieksekusi
ini berguna jika ingin mendebug fungsi yang ada didalam file tersebut
"""
print(wow('hehehe'))