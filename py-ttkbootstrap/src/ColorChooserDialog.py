from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def cc():
	color = ColorChooserDialog()
	color.show()
	# result
	colors = color.result
	label.config(text=colors.hex) # colors.hex, colors.rgb
	# set root background
	root.configure(background=colors.hex)

# Button
button = tb.Button(root, text='choose color', command=cc).pack(pady=10)

# Label
label = tb.Label(root)
label.pack(pady=10)

root.mainloop()