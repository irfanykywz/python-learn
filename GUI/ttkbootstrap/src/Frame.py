from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function

# Frame
frame = tb.Frame(root, bootstyle='info')
frame.pack(pady=10,padx=10,fill=X)

# Entry
entry = tb.Entry(frame)
entry.pack(pady=10)

# Button
button = tb.Button(frame, text='Click')
button.pack(pady=10)

# Label
label = tb.Label(root, text='Text Label')
label.pack(pady=10)

root.mainloop()