import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("black")
alex.pensize(10)
tina = turtle.Turtle()
tina.color("brown")
tina.pensize(12)

 # Creation of base for flag

alex.forward(75)
alex.left(180)
alex.forward(150)
alex.left(180)
alex.forward(150)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(150)
alex.right(90)
alex.forward(50)
alex.left(180)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.left(180)
alex.forward(250)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(250)
alex.right(90)
alex.forward(50)
alex.left(180)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(350)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)

# Creation of actual flag

tina.left(90)
tina.forward(300)
tina.right(90)
tina.forward(200)
tina.right(90)
tina.forward(40)
tina.right(90)
tina.forward(200)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(200)
tina.right(90)
tina.forward(40)
tina.right(90)
tina.forward(200)
tina.left(180)
tina.forward(200)
tina.left(90)
tina.forward(80)
wn.exitonclick()