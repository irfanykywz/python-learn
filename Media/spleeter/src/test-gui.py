# https://stackoverflow.com/questions/68797634/after-packaging-a-python-program-with-pyinstaller-it-shows-that-the-module-i-im
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from spleeter import separator
import tkinter as TKT
from tkinter import ttk
from tkinter import messagebox

window = TKT.Tk()
screen_width,screen_height = window.maxsize()
window.title("Spleeter GUI Version")
w = int((screen_width-700)/2)
h = int((screen_height-400)/2)
window.geometry(f'700x400+{w}+{h}')

lbl = TKT.Label(window, text="File Path:")
lbl.grid(column=0, row=0)

txt = TKT.Entry(window, width=10)
txt.grid(column=1, row=0)

lbl2 = TKT.Label(window, text="Stems:")
lbl2.grid(column=0, row=1)

combo = ttk.Combobox(window)
combo['values'] = (2,4,5)
combo.current(0)
combo.grid(column=1, row=1)

def Separation():
    File_name=txt.get();
    stems='spleeter:'+combo.get()+'stems'
    sep = separator.Separator(stems)
    messagebox.showinfo("Notification", "Separation working!")
    sep.separate_to_file(File_name, 'out')
    messagebox.showinfo("Notification", "Separation Finished!")


def clicked():
    Separation()

btn = TKT.Button(window, text="Separate", command=clicked)
btn.grid(column=2, row=0)

def main():
    window.mainloop()

if __name__=='__main__':
    main()