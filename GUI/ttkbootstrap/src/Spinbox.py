from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def buttonAct():
	label.config(text=spin.get())

# SpinBox
keju = ['Keju Mozarela','Keju Manis','Keju Asin']
spin = tb.Spinbox(root,
	from_=0,
	to=10,
	values=keju,
	state='readonly',
	command=buttonAct
	)
spin.pack(pady=10)

# Button
button = tb.Button(root, text='Submit', command=buttonAct).pack(pady=10)

# Label
label = tb.Label(root)
label.pack(pady=10)

root.mainloop()