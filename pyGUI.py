import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
import serial

#find open ports
import serial.tools.list_ports
for i in serial.tools.list_ports.comports():
    ports = (str(i).split(" ")[0])


#define functions
#clsoe the app
def closeAPP():
        global window
        window.destroy()


def linkUSB():
    linked = True
    openPort = availPorts.get()
    global ser 
    ser = serial.Serial(openPort, 9600)
    print(ser)
    return ser


def setLedHigh():
    #serVariable = availPorts.get()
    #ser = linkUSB()
    ser.write(bytes('H', 'UTF-8'))

def setLedLow():
    #ser = linkUSB()
    ser.write(bytes('L', 'UTF-8'))


#declare and set window namee
window = Tk(className='Arduino Widget')

# enter all code here

#set window size
window.geometry("800x600")

#dropdown menu
n = tk.StringVar()
availPorts = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
availPorts['values'] = ports
  
availPorts.grid(column = 1, row = 5)
availPorts.current()



#button
#linkBtn = Button (LEFT, text = "link board", command = linkBoard )
linkBtn = tkinter.Button (window, text = "link board", command = linkUSB)
closeBtn = tkinter.Button (window, text = "close app", command = closeAPP)
ledOnBtn = tkinter.Button (window, text = "LED on", command = setLedHigh)
ledOffBtn = tkinter.Button (window, text = "LED off", command = setLedLow)

#add button to the window
linkBtn.place(x=250, y = 15)
ledOnBtn.place(x=10, y=80)
ledOffBtn.place(x=120, y=80)
availPorts.place(x = 10, y = 20)
closeBtn.place (x=350, y=550)

#call loop
window.mainloop()   #nothing executes after this main function to call the window




