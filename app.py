from tkinter import font
import serial
import time
import tkinter
from tkinter import *
import customtkinter
import tkinter.ttk as ttk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Control Center")
app.geometry("1280x720")
arduinoData = serial.Serial('COM3',9600)

## Buildings Light Switch
building_state = customtkinter.StringVar(value="on")
def building_switch_event():
    #print("switch toggled, current value:", building_state.get())
    if building_state.get() == "on":
        print("on")
        arduinoData.write('buildings_ON').encode()
    else: 
        arduinoData.write('buildings_OFF').encode()
        print("off")
building_switch = customtkinter.CTkSwitch(master=app, text="Building Lights", command=building_switch_event, variable=building_state, onvalue="on", offvalue="off", width=int(50), height= int(25))
building_switch.grid(row=2,column=1, sticky = W, padx = (10,10), pady = (30,10) )


## Street Lights Switch
street_state = customtkinter.StringVar(value="on")
def street_switch_event():
    #print("switch toggled, current value:", building_state.get())
    if street_state.get() == "on":
        print("on")
        arduinoData.write('street_ON').encode()
    else: 
        arduinoData.write('street_OFF').encode()
        print("off")
street_switch = customtkinter.CTkSwitch(master=app, text="Street Lights", command=street_switch_event, variable=street_state, onvalue="on", offvalue="off", width=int(50), height= int(25))
street_switch.grid(row=3,column=1, sticky = W, padx = (10,10), pady = (10,10))



## Operating Accessories Switch
operating_acc_state = customtkinter.StringVar(value="on")
def operating_acc_event():
    #print("switch toggled, current value:", building_state.get())
    if operating_acc_state.get() == "on":
        print("on")
        arduinoData.write('acc_ON').encode()
    else: 
        arduinoData.write('acc_OFF').encode()
        print("off")
operating_acc_switch = customtkinter.CTkSwitch(master=app, text="Operating Accessories", command=operating_acc_event, variable=operating_acc_state, onvalue="on", offvalue="off", width=int(50), height= int(25))
operating_acc_switch.grid(row=4,column=1, sticky = W, padx = (10,10), pady = (10,10))



## Signal Lights Switch
signal_lights_state = customtkinter.StringVar(value="on")
def signal_lights_event():
    #print("switch toggled, current value:", building_state.get())
    if signal_lights_state.get() == "on":
        print("on")
        arduinoData.write('signal_ON').encode()
    else: 
        arduinoData.write('signal_OFF').encode()
        print("off")
signal_lights_switch = customtkinter.CTkSwitch(master=app, text="Signal Lights", command=signal_lights_state, variable=signal_lights_state, onvalue="on", offvalue="off", width=int(50), height= int(25))
signal_lights_switch.grid(row=5,column=1, sticky = W, padx = (10,10), pady = (10,10))


app.mainloop()