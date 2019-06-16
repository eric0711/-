from tkinter import *

window = Tk()

window.title("만들기 어렵다")
canvas = Canvas(window, height=200, width=200)

canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)

def mouseClick(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y

    canvas.create_line(x1, y1, x2, y2, width=5, fill="blue")

canvas.pack()
window.mainloop()