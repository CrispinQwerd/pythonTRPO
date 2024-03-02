import turtle

screen = turtle.Screen()
star = turtle.Turtle()

star.penup()
star.goto(-100, 0)
star.pendown()
star.speed(10) 

for n in range(9):
    star.forward(100) 
    star.right(160)
    
turtle.done()