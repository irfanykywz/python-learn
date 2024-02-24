
def wow(a):
	return a

# ketika dijalankan sebagai module maka akan menghasilkan nilai nama file = program
# ketika dijalankan langsung maka akan menghasilkan nilai = __main__ 
print(__name__)

# membandingkan jika name == main
if __name__ == '__main__':
	print('run')