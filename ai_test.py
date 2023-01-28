#install tutor in ubuntu20.04
import turtle

# Set up the window and its attributes
turtle.setup(800, 600)
turtle.bgcolor("black")
turtle.title("Iron Man")
turtle.hideturtle()

# Draw the head of Iron Man 
turtle.penup()  # Lift the pen so it doesn't draw while moving to the starting position 
turtle.goto(-200, 200)  # Move to the starting position 
turtle.pendown()  # Put the pen down so it can draw while moving around 
turtle.fillcolor("red")  # Set the fill color to red 
turtle.begin_fill()  # Begin filling in with this color 
for i in range(2):   # Draw a circle for Iron Man's head  
  turtle.circle(100)   # Radius of 100 pixels  
  turtle.right(90)   # Turn right 90 degrees  
  turtle.forward(200)   # Move forward 200 pixels  
  turtle.right(90)   # Turn right 90 degrees again  
turtle.end_fill()   # End filling with this color 

# Draw Iron Man's eyes and mouth 

turtle.penup()  # Lift the pen so it doesn't draw while moving to the starting position for eyes and mouth 

turtle.goto(-150, 250)  # Move to the starting position for eyes and mouth

turtle.pendown()   # Put the pen down so it can draw while moving around for eyes and mouth

turtle.fillcolor("white")    # Set fill color to white for eyes and mouth

turtle.begin_fill()     # Begin filling with white color for eyes and mouth

turtle.circle(10)     # Draw a circle with radius 10 pixels for left eye of Iron Man

turtle.end_fill()      # End filling with white color for left eye of Iron Man

turtle.penup()        # Lift pen so it doesn't draw while moving to right eye's starting position of Iron Man

turtle