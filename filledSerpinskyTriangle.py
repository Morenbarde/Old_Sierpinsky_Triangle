#Old Project from first CS Class, displays a serpinsky triangle if different levels based on input

from tkinter import *

def displayPolygon(p1, p2, p3, p4, p5, p6):
    canvas.create_polygon(p1, p2, p3, p4, p5, p6,
                          tags = "triangle", fill = "black")
    return

def display():
    canvas.delete("triangle")
    p1 = [width/2, 10]
    p2 = [10, height - 10]
    p3 = [width - 10, height - 10]
    displayTriangles(int(order.get()), p1, p2, p3)
    order.set("")
    return

def displayTriangles(order, p1, p2, p3):
    


    if order == 0:
        displayPolygon(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
    else:
        p12 = midpoint(p1, p2)
        p13 = midpoint(p2, p3)
        p14 = midpoint(p3, p1)

        displayTriangles(order - 1, p1, p12, p14)
        displayTriangles(order - 1, p2, p12, p13)
        displayTriangles(order - 1, p3, p13, p14)

def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p

window = Tk()
window.title("Filled Serpinsky Triangle")

width = 700
height = 700
canvas = Canvas(window, width = width, height = height)
canvas.pack()

frame1 = Frame(window)
frame1.pack()

Label(frame1, text = "Enter an order: ").pack(side = LEFT)
order = StringVar()
entry = Entry(frame1, textvariable = order, justify = RIGHT).pack(side = LEFT)
Button(frame1, text = "Display Serpinsky Triangle", command = display).pack(side = LEFT)

window.mainloop()
