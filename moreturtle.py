import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.up()

for i in range(10):
    alex.forward(50)
    alex.stamp()
    alex.forward(-50)
    alex.right(36)

wn.exitonclick()