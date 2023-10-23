from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function

# Text
text = ScrolledText(root, height=20, width=100, wrap=WORD, autohide=True, hbar=False)
text.pack(pady=10)

# Button

# Label

root.mainloop()