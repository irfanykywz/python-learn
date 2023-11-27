from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function button
def buttonAct():
	label.config(text=f'You Select {combobox.get()}')

# function combobox
def comboboxAct(e):
	label.config(text=f'Select {combobox.get()}')

# label
label = tb.Label(text='ComboBox TTK Bootstrap', font=('Helvatica',28), bootstyle='primary')
label.pack(pady=50)

#option
seasons = ['Spring','Summer','Autumn','Winter']

# combobox
combobox = tb.Combobox(root, 
	bootstyle='primary',
	values=seasons)
combobox.pack(pady=10)
combobox.current(0)

# button
button = tb.Button(text='Kirim', command=buttonAct)
button.pack(pady=10)

# bind
combobox.bind('<<ComboboxSelected>>', comboboxAct)

root.mainloop()