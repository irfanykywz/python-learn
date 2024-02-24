"""
ternary operator yaitu pengkondisian dalam 1 baris saja
"""

grade = 65

# penggunaan langsung
if grade >= 65: print("passed the exam")

# penggunaan di print
print('lulus' if grade >= 65 else 'tidak lulus')

# penggunaan di variable
status = 'lulus' if grade >= 65 else 'tidak lulus'
print(status)