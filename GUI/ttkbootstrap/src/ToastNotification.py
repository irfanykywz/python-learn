from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification 

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function 
def toasted():
	toast.show_toast()

# toast
toast = ToastNotification(title = 'Hehehe boi',
	message='Anda dapat jackpot 100JT',
	duration=3000,
	alert=True,
	position=('bottom')
	)

# button
button = tb.Button(root, text='show toast', command=toasted).pack(pady=10)

root.mainloop()