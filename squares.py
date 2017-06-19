import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.up()
def Makesquare(al: object, steps: object) -> object:

    for i in ["red","lightgreen","blue","brown","pink","green","black"]:
        alex.shape("turtle")
        steps = steps + 15
        al.pensize(2)
        al.color(i)
        alex.stamp()
        al.forward(steps)
        al.right(25)

n = int(input("Enter the initial step"))
print(type(n))

for j in range(15):

    Makesquare(alex,n)
    alex.goto(10,10)


wn.exitonclick()