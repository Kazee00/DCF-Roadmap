import turtle
distance=100
degree=90

square = turtle.Turtle()
square.color("red")
square.begin_fill()


square.forward(distance)
square.left(degree)
square.forward(distance)
square.left(degree)
square.forward(distance)
square.left(degree)
square.forward(distance)
square.left(degree)

square.end_fill()

turtle.done()