from tkinter import *
import tkinter as tk
from PIL import ImageTk
import gettingstarted2

root = tk.Tk()

canvas = Canvas(root, width = 1300, height = 690, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "/Users/Garrett/Desktop/PythonGUI/PughHall.gif")
canvas.create_image(10,10, image = image, anchor = NW)

def openGraph(root):
    Graph = gettingstarted2.py
    iconEntry.insert(0, graph)

sensor1 = tk.Button(root, text='', bg = "green", command = openGraph, anchor = W)
sensor1.place(x=40, y=160)

sensor2 = tk.Button(root, text='', bg = "green", command = openGraph)
sensor2.place(x=80, y=250)


mainloop()
