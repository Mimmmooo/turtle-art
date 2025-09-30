import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Cute Pikachu")

pikachu = turtle.Turtle()
pikachu.speed(7)
pikachu.pensize(2)

def my_goto(x, y):
    pikachu.penup()
    pikachu.goto(x, y)
    pikachu.pendown()

def circle(color, radius, x, y):
    my_goto(x, y - radius)
    pikachu.fillcolor(color)
    pikachu.begin_fill()
    pikachu.circle(radius)
    pikachu.end_fill()

def ears():
    pikachu.fillcolor("black")
    pikachu.begin_fill()
    my_goto(-60, 150)
    pikachu.setheading(150)
    pikachu.circle(40, 70)
    pikachu.setheading(230)
    pikachu.circle(40, 70)
    pikachu.end_fill()

    pikachu.begin_fill()
    my_goto(60, 150)
    pikachu.setheading(30)
    pikachu.circle(-40, 70)
    pikachu.setheading(-50)
    pikachu.circle(-40, 70)
    pikachu.end_fill()

def face():
    pikachu.fillcolor("gold")
    pikachu.begin_fill()
    pikachu.circle(120)
    pikachu.end_fill()

def eyes():
    circle("white", 25, -50, 70)
    circle("white", 25, 50, 70)
    circle("black", 12, -50, 70)
    circle("black", 12, 50, 70)
    circle("white", 5, -55, 75)
    circle("white", 5, 45, 75)

def cheeks():
    circle("red", 20, -80, 30)
    circle("red", 20, 80, 30)

def nose():
    circle("black", 8, 0, 55)

def mouth():
    my_goto(-40, 40)
    pikachu.setheading(-60)
    pikachu.circle(40, 120)

ears()
face()
eyes()
cheeks()
nose()
mouth()

pikachu.hideturtle()
screen.mainloop()
