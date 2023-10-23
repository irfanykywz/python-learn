from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def yesno():
	messagebox = Messagebox.yesno('Apakah kamu yakin ingin jadi anime ?')
	label.config(text=f'you click {messagebox}')
def okcancel():
	messagebox = Messagebox.okcancel('Apakah kamu yakin ingin jadi anime ?')
	label.config(text=f'you click {messagebox}')	
def show_info():
	messagebox = Messagebox.show_info('Kamu berhasil jadi anime', 'Peringatan !!')	
def show_error():
	messagebox = Messagebox.show_error('Kamu gagal jadi anime', 'Peringatan !!')	
def show_warning():
	messagebox = Messagebox.show_warning('Kamu gagal jadi anime', 'Peringatan !!')	
def show_question():
	messagebox = Messagebox.show_question('Kamu berhasil jadi anime', 'Peringatan !!')	
def yesnocancel():
	messagebox = Messagebox.yesnocancel('Kamu berhasil jadi anime', 'Peringatan !!')	
def retrycancel():
	messagebox = Messagebox.retrycancel('Kamu berhasil jadi anime', 'Peringatan !!')			


# Button
buttonyesno = tb.Button(root, text='Message Box Yes No', command=yesno).pack(pady=10)
buttonokcancel = tb.Button(root, text='Message Box Cancel OK', command=okcancel).pack(pady=10)
buttonshow_info = tb.Button(root, text='Message Box Show Info', command=show_info).pack(pady=10)
buttonshow_error = tb.Button(root, text='Message Box Show Error', command=show_error).pack(pady=10)
buttonshow_warning = tb.Button(root, text='Message Box Show Warning', command=show_warning).pack(pady=10)
buttonshow_question = tb.Button(root, text='Message Box Show Question', command=show_question).pack(pady=10)
buttonyesnocancel = tb.Button(root, text='Message Box Yes No Cancel', command=yesnocancel).pack(pady=10)
buttonretrycancel = tb.Button(root, text='Message Box Yes No Cancel', command=retrycancel).pack(pady=10)


# Label
label = tb.Label(root)
label.pack(pady=40)

root.mainloop()