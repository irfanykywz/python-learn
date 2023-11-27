from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def buttonAct():
	label.config(text=f'Anda memilih : {var.get()}')

# Radio Button
martabaks = ['Martabak Mini','Martabak Telor','Martabak Keju']

var = StringVar()
for martabak in martabaks:
	tb.Radiobutton(root, variable=var, text=martabak, value=martabak,
		command=buttonAct
		).pack(pady=10)


# Button
button = tb.Button(root, text='Pilih', command=buttonAct).pack(pady=10)

# Label
label = tb.Label(root, text='')
label.pack(pady=20)

root.mainloop()