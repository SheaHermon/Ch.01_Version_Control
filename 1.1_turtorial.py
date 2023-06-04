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
screen.screensize(250,250)
Lightsaber.speed(5)
Lightsaber.shape("turtle")
Lightsaber.color("black")
Lightsaber.fillcolor("grey")
Lightsaber.penup()
Lightsaber.goto(-25,-150)
Lightsaber.pendown()
Lightsaber.begin_fill()
Lightsaber.forward(50)
Lightsaber.right(90)
Lightsaber.forward(20)
Lightsaber.right(90)
Lightsaber.forward(50)
Lightsaber.right(90)
Lightsaber.forward(20)
Lightsaber.end_fill()
Lightsaber.penup()
Lightsaber.goto(-15,-150)
Lightsaber.pendown()
Lightsaber.begin_fill()
Lightsaber.forward(100)
Lightsaber.right(90)
Lightsaber.forward(30)
Lightsaber.right(90)
Lightsaber.forward(100)
Lightsaber.right(90)
Lightsaber.forward(30)
Lightsaber.end_fill()
Lightsaber.penup()
Lightsaber.goto(-25,-50)
Lightsaber.pendown()
Lightsaber.begin_fill()
Lightsaber.right(180)
Lightsaber.forward(50)
Lightsaber.right(90)
Lightsaber.forward(20)
Lightsaber.right(90)
Lightsaber.forward(50)
Lightsaber.right(90)
Lightsaber.forward(20)
Lightsaber.end_fill()
Lightsaber.penup()
Lightsaber.goto(-12,-50)
Lightsaber.color("pink")
Lightsaber.fillcolor("red")
Lightsaber.begin_fill()
Lightsaber.pendown()
Lightsaber.forward(200)
Lightsaber.circle(-12,180)
Lightsaber.forward(200)
Lightsaber.end_fill()
Lightsaber.penup()
Lightsaber.goto(25,-55)
Lightsaber.begin_fill()
Lightsaber.pendown()
Lightsaber.left(90)
Lightsaber.forward(50)
Lightsaber.circle(-5,180)
Lightsaber.forward(50)
Lightsaber.end_fill()
Lightsaber.penup()
Lightsaber.goto(-25,-55)
Lightsaber.begin_fill()
Lightsaber.pendown()
Lightsaber.forward(50)
Lightsaber.circle(5,180)
Lightsaber.forward(50)
Lightsaber.end_fill()
Lightsaber.penup()




Lightsaber.write('Shea Hermon',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
