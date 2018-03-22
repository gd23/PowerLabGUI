from tkinter import *
import tkinter as tk
from PIL import ImageTk
import gettingstarted2

canvas = Canvas(width = 1300, height = 690, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "/Users/Garrett/Desktop/PythonGUI/PughHall.gif")
canvas.create_image(10,10, image = image, anchor = NW)

root = tk.Tk()
app = Frame(root)
Frame.pack()

def openGraph(root):
    Graph = gettingstarted2.py
    iconEntry.insert(0, graph)

button1 = tk.Button(frame, text='', fg = "green", command = openGraph)
button1.pack(side=tk.LEFT)


mainloop()
