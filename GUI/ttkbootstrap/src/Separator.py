from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# Label
label1 = tb.Label(root, text='Label 1').pack(pady=10)

# Separator
separator = tb.Separator(root,
	orient="horizontal"
	).pack(fill='x')

# Label
label2 = tb.Label(root, text='Label 2').pack(pady=10)

root.mainloop()