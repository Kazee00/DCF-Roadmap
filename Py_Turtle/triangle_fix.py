# Step 1 : Import the turtle Module / Library
import turtle

# Step 2 : Create a turtle object/variable to control
triangle = turtle.Turtle()

# Step 3 : Draw around using turtle methods
#Using Function Concept to Draw Customize Triangle with Color and Lenght
#triangle 1
triangle.fillcolor("skyblue")
triangle.begin_fill()

triangle.forward(300)
triangle.left(120)

triangle.forward(300)
triangle.left(120)

triangle.forward(300)
triangle.left(120)

triangle.end_fill()

#triangle 2
triangle.fillcolor("red")
triangle.begin_fill()

triangle.forward(150)
triangle.left(120)

triangle.forward(150)
triangle.left(120)

triangle.forward(150)
triangle.left(120)

triangle.end_fill()



# Step 4 : Prevent the Output Screen from Closing turtle.done()
turtle.done()