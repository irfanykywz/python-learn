from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='cyborg')
# root = Tk()
root.title('TTK Bootstrap')
# root.iconbitmap('icon.ico')
root.geometry('500x350')

# function
def start():
	floodgauge.start()
def stop():
	floodgauge.stop()	
def increment():	
	floodgauge.step()
	label.config(text=f'Position: {floodgauge.variable.	get()}')

# floodgauge
floodgauge = tb.Floodgauge(root,
	bootstyle='light',
	mask='Process {}%',
	maximum=100,
	orient='horizontal',
	value=0,
	mode='determinate'
	)
floodgauge.pack(pady=10, padx=10, fill=X)

# Button
startButton = tb.Button(root, text='Start', command=start)  
startButton.pack(pady=10, padx=10, fill=X)

stopButton = tb.Button(root, text='Stop', command=stop) 
stopButton.pack(pady=10, padx=10, fill=X) 

incementButton = tb.Button(root, text='Increment', command=increment) 
incementButton.pack(pady=10, padx=10, fill=X) 

# Label
label = tb.Label(root, text='Position: ')
label.pack(pady=10, padx=10, fill=X)

root.mainloop()