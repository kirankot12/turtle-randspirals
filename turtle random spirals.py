import colorsys
import random 
import turtle 
turtle.bgcolor("black")
colors = ["red", "green", "purple", "orange", "yellow", "white", "gray", "blue"]
for n in range(50):
    turtle.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(-turtle.window_width()//2,
                        turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                        turtle.window_height()//2)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for m in range(size):
        turtle.forward(m*2)
        turtle.left(91)