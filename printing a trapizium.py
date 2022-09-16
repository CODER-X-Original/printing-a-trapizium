from shutil import move
import turtle

move = turtle.Turtle()

move.color("red") # Choose colour from here
move.pensize(5) # Size of your pen
move.shape('turtle')

def making_a_trapizium() :
 move.right(80) # Angle 
 move.forward(300) # The size of the line
 move.right(100) # Angle 
 move.forward(250) # The size of the line 
 move.right(100) # Angle 
 move.forward(300) # The size of the line
 move.right(80)
 move.forward(145)

making_a_trapizium()