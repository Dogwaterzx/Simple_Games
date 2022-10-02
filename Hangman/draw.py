# Draws the Hang Man figure and codes it to interact with the character guessings.
# Helper functions for drawing with Turtle

import turtle 
screen = turtle.Screen()

# Changes background picture to image
# image is a string (ex. "beach.jpg")


# Returns new turtle with the shape of image
# image is a string (ex. "shark.png")
def newturtle(image): 
  screen.addshape(image)
  t = turtle.Turtle()
  t.shape(image)
  return t

#############
# drawword() function writes text on the screen
# text is a string
w = turtle.Turtle()
w.ht()
w.color("black")              # change font color 
def drawword(text): 
  w.clear()
  w.up()
  w.goto(-150, -100)
  w.write(text, font=("Arial", 40, "bold"))  
##############
