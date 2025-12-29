# Source - https://stackoverflow.com/q
# Posted by Thinh Phuc Vang, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-28, License - CC BY-SA 4.0

import turtle
turtle.bgcolor("#ffd500")
draw = turtle.Turtle()
draw.speed(1000000)
draw.hideturtle()
draw.pensize(3)
draw.color("#fa0202")

def mm (x, y, forwardLen):
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    for i in range (0, 4):
        draw.forward(forwardLen)
        draw.right(90)

x =-40
y = -40
forwardLen = 40
for i in range (0, 10):
    for j in range (0, 10):
         mm ( x + j*forwardLen, y + i*forwardLen, forwardLen)

turtle.done()
