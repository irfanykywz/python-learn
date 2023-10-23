from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def buttonAct():
	label.config(text=f'Date Picked : {date.entry.get()}')

def buttonDialogAct():
	cal = Querybox()
	label.config(text=f'Date Picked : {cal.get_date()}')

# DateEntry
date = tb.DateEntry(root,
	firstweekday=0,
	startdate=date(2023, 8, 30)
	)
date.pack(pady=10)

# Button
button = tb.Button(root, text='Get Date',
	command=buttonAct)
button.pack(pady=10)

# get Date by click Button
buttonDialog = tb.Button(root, text='Get Date Querybox',
	command=buttonDialogAct)
buttonDialog.pack(pady=10)

# Label
label = tb.Label(root, text='')
label.pack(pady=10)


root.mainloop()