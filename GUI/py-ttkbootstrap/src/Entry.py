from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def buttonAct():
	label.config(text=f'Input result : {entry.get()}')

# Entry
entry = tb.Entry(root, bootstyle='success',
	font=('Helvatica', 20),
	foreground='white',
	width='10',
	show="*" # hide text
	)
entry.pack(pady=10)

# Button
button = tb.Button(root, text='Submit', command=buttonAct)
button.pack(pady=10)

#label 
label = tb.Label(root)
label.pack(pady=10)

root.mainloop()