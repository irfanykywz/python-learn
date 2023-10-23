from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def buttonAct():
	label.config(text=f'Process')

# Label
label = tb.Label(root)
label.pack(pady=10)

# Text
text = tb.Text(root, width=70, height=10)
text.pack(pady=10)

# Button
button = tb.Button(root, text='Created', command=buttonAct)
button.pack(pady=10)

root.mainloop()