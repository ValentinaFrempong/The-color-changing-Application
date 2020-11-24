
import tkinter as tk
from tkinter import ttk

myWindow = tk.Tk()
myWindow.title("The color changer")

myWindow.configure(background="#de9f0d")

ttk.Label(myWindow, text="Enter your name").grid(column=0,row=0)

def click_me():
    button.configure(text="Hello " + name.get())

name = tk.StringVar()
name_enter = ttk.Entry(myWindow, width=15, textvariable = name)
name_enter.grid(column=0,row=1)

button = ttk.Button(myWindow, text="Click Me", command= click_me)
button.grid(column=1,row=1)

color1 = "#9971b0"
color2 = "#6da5a8"
color3 = "#77a368"

def radio_call():
    selection = radioButton.get()
    if selection == 1 : myWindow.configure(background=color1)
    elif selection == 2 : myWindow.configure(background=color2)
    elif selection == 3 : myWindow.configure(background=color3)

radioButton = tk.IntVar()

radio1 = tk.Radiobutton(myWindow, text="First" ,variable=radioButton, value= 1, command=radio_call)
radio1.grid(column=0, row=3, sticky=tk.W,columnspan=3)

radio2 = tk.Radiobutton(myWindow, text="Second" ,variable=radioButton, value= 2, command=radio_call)
radio2.grid(column=1, row=3, sticky=tk.W,columnspan=3)

radio3 = tk.Radiobutton(myWindow, text="Third", variable=radioButton, value= 3, command=radio_call)
radio3.grid(column=2, row=3, sticky=tk.W,columnspan=3)
