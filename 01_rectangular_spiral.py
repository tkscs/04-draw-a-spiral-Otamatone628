import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
x = 90

def spiral (size) :
    for i in range(10, size, 10) :
        turtle.forward(i)
        turtle.left(x)

spiral(100)


### YOUR CODE ENDS HERE

turtle.exitonclick()