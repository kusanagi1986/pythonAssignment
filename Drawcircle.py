
#import tkinter
import tkinter as tk
win = tk.Tk()

#import turtle
import turtle

screen=turtle.Screen()
screen.bgcolor("yellow")
drawPen=turtle.Pen()
drawPen.pensize(3)
drawPen.color("red")
drawPen.penup()
drawPen.goto(0,-270)
drawPen.pendown()

drawPen.circle(5*50)
drawPen.penup()
drawPen.goto(0,0)
drawPen.pendown()
drawPen.forward(5*50)

turtle.mainloop()
