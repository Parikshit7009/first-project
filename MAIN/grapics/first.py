import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("white")
t.pencolor("black")

a=0
b=0
t.speed(0)
t.penup()
t.goto(0,100)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=1
    b+=3
    if b==500:
        break
    t.hideturtle()
turtle.done()
