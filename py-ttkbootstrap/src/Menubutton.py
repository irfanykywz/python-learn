from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def actionClick(x):
	label.config(text=x)

# Menubutton
menu = tb.Menubutton(root, text='Dropdown')
menu.pack(pady=50)

menuList = tb.Menu(menu)

itemVar = StringVar()
for x in ['Tomato','Egg','Milk']:
	 menuList.add_radiobutton(label=x, variable=itemVar, 
	 	command=lambda x=x: actionClick(x))

menu['menu'] = menuList

# Label
label = tb.Label(root)
label.pack(pady=10)

root.mainloop()