from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('700x350')

# function

# tree
columns = ('id','nama','harga')
tree = tb.Treeview(root,
	columns=columns,
	show='headings',
	bootstyle='light'
	)
tree.pack(pady=10)
tree.heading('id', text='id')
tree.heading('nama', text='nama')
tree.heading('harga', text='harga')

# data
data = []
for n in range(1,100):
	data.append((f'ID {n}', f'Nama {n}', f'Harga {n}'))

for dat in data:
	tree.insert('', END, values=dat)

# Button

# Label

root.mainloop()