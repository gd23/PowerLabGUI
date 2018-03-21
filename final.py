from tkinter import *
import tkinter as tk
from PIL import ImageTk
import gettingstarted2

root = Tk()

canvas = Canvas(width = 1300, height = 690, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "/Users/Garrett/Desktop/PythonGUI/PughHall.gif")
canvas.create_image(10,10, image = image, anchor = NW)

app = Frame(root)

def openGraph(root):
    Graph = gettingstarted2.py
    iconEntry.insert(0, graph)

button1 = Button(app, bg = "green")
button1.pack()




mainloop()
