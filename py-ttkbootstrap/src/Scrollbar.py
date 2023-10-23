from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function

# Frame
frame = tb.Frame(root)
frame.pack(pady=10,padx=10,fill=X)

# Scroll
scroll = tb.Scrollbar(frame,
	orient='vertical',
	)
scroll.pack(side='right',fill='y')

# Text
text = Text(frame, width=30, height=30,
	yscrollcommand=scroll.set,
	wrap='none',
	font=('Helvatica',18)
	)
text.pack(fill=X)

# Scroll config
scroll.config(command=text.yview)

# Button

# Label

root.mainloop()