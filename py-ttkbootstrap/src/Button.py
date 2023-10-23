from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function button
counter = 0
def buttonAct():
	global counter
	counter += 1
	if counter % 2 == 0:
		label.config(text='Do Scrape')
	else:
		label.config(text='Stop Scrape')

# label
label = tb.Label(text='Button TTK Bootstrap', font=('Helvatica',28), bootstyle='primary')
label.pack(pady=50)

# button
button = tb.Button(text='Buat', bootstyle='primary, outline', command=buttonAct)
button.pack(pady=10)

# style
style = tb.Style()
style.configure('danger.Outline.TButton', font=("Helvatica",18))

# big button
big = tb.Button(text='Buat', 
	style="danger.Outline.TButton",
	command=buttonAct)
big.pack(pady=10)

root.mainloop()