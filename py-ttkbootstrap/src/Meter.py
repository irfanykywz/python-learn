from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function

# Meter
meter = tb.Meter(root, 
	bootstyle='danger',
	subtext='Metered')
meter.pack(pady=10)

# Button

# Label

root.mainloop()