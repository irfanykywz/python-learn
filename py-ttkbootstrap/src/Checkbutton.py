from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function checkbox
counter = 0
def checkboxAct():
	if varcheck.get() == 1:
		label.config(text='Checked')
	else:
		label.config(text='Unchecked')

# label
label = tb.Label(text='Checkbox TTK Bootstrap', font=('Helvatica',28), bootstyle='primary')
label.pack(pady=(40,10))

# checkbox
varcheck = IntVar()
checkbox = tb.Checkbutton(text='Ceklis', 
	bootstyle='primary', 
	variable=varcheck,
	onvalue=1,
	offvalue=0,
	command=checkboxAct)
checkbox.pack(pady=10)


# switch
checkboxSwitch = tb.Checkbutton(text='Ceklis', 
	bootstyle='primary, round-toggle', 
	variable=varcheck,
	onvalue=1,
	offvalue=0,
	command=checkboxAct)
checkboxSwitch.pack(pady=10)

# switch square
checkboxSwitch = tb.Checkbutton(text='Ceklis', 
	bootstyle='primary, square-toggle', 
	variable=varcheck,
	onvalue=1,
	offvalue=0,
	command=checkboxAct)
checkboxSwitch.pack(pady=10)

root.mainloop()