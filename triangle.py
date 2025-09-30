import turtle

pen = turtle.Turtle()
pen.speed(1000)  #drawing speed
pen.shape("turtle") 

def draw_triangle(x1, x2, x3):
    pen.penup()
    pen.goto(x1)
    pen.pendown()
    pen.goto(x2)
    pen.goto(x3)
    pen.goto(x1)

def sierpinski(x1, x2, x3, level):
    if level == 0:
        draw_triangle(x1, x2, x3)
    else:
        mid1 = ((x1[0] + x2[0]) / 2, (x1[1] + x2[1]) / 2)
        mid2 = ((x2[0] + x3[0]) / 2, (x2[1] + x3[1]) / 2)
        mid3 = ((x3[0] + x1[0]) / 2, (x3[1] + x1[1]) / 2)

        sierpinski(x1, mid1, mid3, level - 1)
        sierpinski(mid1, x2, mid2, level - 1)
        sierpinski(mid3, mid2, x3, level - 1)

x1 = (-300, -300)
x2 = (0, 300)
x3 = (300, -300)

sierpinski(x1, x2, x3, 6)
pen.hideturtle()
turtle.done
