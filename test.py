import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5, 60, 2))
tess.up()                     # this is new

for i in range(5):

    tess.forward(50)
    tess.stamp()

wn.exitonclick()