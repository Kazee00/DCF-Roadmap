import turtle

Screen = turtle.Screen()
Screen.bgcolor("black")

distance = 100
degree = 144


turtle.fillcolor("yellow")

turtle.color("yellow")
turtle.begin_fill()
# Use a loop to draw the star
for _ in range(5):  # A star has 5 points
    turtle.forward(distance)
    turtle.right(degree)
turtle.end_fill()
turtle.done()