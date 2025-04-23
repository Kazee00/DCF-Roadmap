import turtle
sin = turtle.Turtle()
sin.pensize(5)

sin.penup()
sin.goto(-57, 60)
sin.pendown()
sin.setheading(0)
sin.forward(120)
sin.left(120)
sin.forward(120)
sin.right(-120)
sin.forward(120)
sin.hideturtle()

name = "Triangle"
turtle.write(f'{name}', align='center', font=("Oswald", 20, "italic"))
turtle.hideturtle()

turtle.done()