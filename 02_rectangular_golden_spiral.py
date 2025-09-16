import turtle
from scipy.constants import golden as phi

"""
In a golden spiral, for every 90 degrees, the arm length of the spiral grows
by a factor of phi (which is approximately 1.618)

So if the spiral has so far turned 90 degrees i times, then the current arm
length will be:

initial_arm_length * (phi**i)
"""

### YOUR CODE STARTS HERE

x = 90

def spiral (size) :
    for i in range (size) :
        turtle.forward(phi**i)
        turtle.left(x)

spiral(13)

### YOUR CODE ENDS HERE

turtle.exitonclick()