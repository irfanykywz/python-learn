from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def Increment():
	# progressbar.step(10)
	progressbar['value'] += 20
	label.config(text=progressbar['value'])
def Start():
	progressbar.start()
def Stop():
	progressbar.stop()
def Auto():
	for x in range(5):
		progressbar['value'] += 20
		label.config(text=progressbar['value'])

		root.update_idletasks()

		time.sleep(1)

# progressbar
progressbar = tb.Progressbar(root,
	maximum=100,
	mode="determinate",
	length=100,
	value=0
	)
progressbar.pack(pady=10,padx=10,fill=X)

# frame
frame = tb.Frame(root)
frame.pack(pady=10)

# Button
button = tb.Button(frame, text='Increment', command=Increment)
button.grid(column=1, row=0, padx=10)

button2 = tb.Button(frame, text='Start', command=Start)
button2.grid(column=2, row=0, padx=10)

button3 = tb.Button(frame, text='Stop', command=Stop)
button3.grid(column=3, row=0, padx=10)

button4 = tb.Button(frame, text='Auto', command=Auto)
button4.grid(column=4, row=0, padx=10)

# Label
label = tb.Label(root)
label.pack(pady=10)

root.mainloop()