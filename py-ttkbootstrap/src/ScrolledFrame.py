from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# Scrollframe
frame = ScrolledFrame(root, autohide=False)
frame.pack(pady=10, padx=10, fill=BOTH, expand=YES)

# Button
for x in range(20):
	tb.Button(frame, text=f'Button {x}').pack(pady=10,padx=10)

root.mainloop()