from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# Label
label1 = tb.Label(root, text='Label 1').pack(pady=10)

# Label
label2 = tb.Label(root, text='Label 2').pack(pady=10)

# Sizegrip
sizegrip = tb.Sizegrip(root, bootstyle='light').pack(anchor='se', fill='both', expand=True)


root.mainloop()