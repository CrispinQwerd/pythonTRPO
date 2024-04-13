import turtle 

t = turtle
t.pensize(3)
turtle.speed(500) 
t.shape("turtle")
r=int(input("Введите радиус первого круга: ->  ")) 
m = 4
colors=["blue","orange","green","red"] 


for i in range(m+1): 
    color = colors[i%4]
    t.circle(r * i) 
    t.up() 
    t.sety((r * i)*(-1)) 
    t.down() 
    t.pencolor(color)


input("Press the Enter key to continue: ")