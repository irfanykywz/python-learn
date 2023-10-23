from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function

# notebook
notebook = tb.Notebook(root)
notebook.pack(pady=10,padx=10,fill=X)

# tab
tab1 = tb.Frame(notebook)
tab2 = tb.Frame(notebook)

# tab1
label = Label(tab1, text='Text on tab 1')
label.pack(pady=10)

# tab2
label2 = Label(tab2, text='Text on tab 2')
label2.pack(pady=10)

# notebook add
notebook.add(tab1, text='tab 1')
notebook.add(tab2, text='tab 2')

root.mainloop()