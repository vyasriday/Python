import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5, 60, 2))
tess.up()                     # this is new
for size in range(5, 60, 2):    # start with size = 5 and grow by 2
                   # leave an impression on the canvas
    tess.stamp()
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()