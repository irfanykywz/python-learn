from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def scaler(e):
	label.config(text=f'{int(scale.get())}')

# Scale
scale = tb.Scale(root,
	length=100,
	orient='horizontal',
	from_=0,
	to=100,
	command=scaler
	)
scale.pack(pady=10)

# Label
label = tb.Label(root, font=('Helvatica',20))
label.pack(pady=10)

root.mainloop()