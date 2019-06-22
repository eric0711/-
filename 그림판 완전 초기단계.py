import tkinter

x1 = None
y1 = None
x2 = None
y2 = None

dm = 0
dc = "red"

def selectButton():
    global dm
    d_color = 0

def pointButton():
    global dm
    dm = 1
def lineButton():
    global dm
    dm = 2

def redButton():
    global dc
    dc = "red"








ang=tkinter.Tk()
ang.title("ang")
ang.geometry("1000x1000")
ang.resizable(False, False)

lb=tkinter.Label(ang, text="welcome to paint program!!")
lb.pack()

ang.mainloop()

