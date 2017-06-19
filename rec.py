import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
#tess.shape("turtle")
tess.color("red")
#print(range(5,100,3))
tess.up()  # It says that each iteration lift the pen
for i in range(5,100,10):
    tess.stamp()
    tess.color("orange")
    tess.forward(i)
    tess.right(90)
tess.color("pink")
wn.exitonclick()