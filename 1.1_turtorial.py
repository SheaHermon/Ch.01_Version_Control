'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
Lightsaber=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('blue') # colors the screen
screen.screensize(500,500)
Lightsaber.speed(1)
Lightsaber.shape("turtle")
Lightsaber.color("black")
Lightsaber.fillcolor("grey")
Lightsaber.penup()
Lightsaber.goto(225,400)
Lightsaber.pendown()
Lightsaber.forward(20)
Lightsaber.right(50)
Lightsaber.back(20)
Lightsaber.left(50)





Lightsaber.write('Shea Hermon',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
