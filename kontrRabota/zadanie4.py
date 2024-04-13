import turtle

square = turtle.Turtle()
square.shape("turtle")

for i in range(180):
    square.speed(1000)
    square.forward(i)
    square.left(91)

input("Press the Enter key to continue: ")
