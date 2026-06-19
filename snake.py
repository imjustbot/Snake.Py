import turtle
import time

SCHERMO = turtle.Screen()
SCHERMO.title("Snake")
SCHERMO.bgcolor("black")
SCHERMO.setup(width=600, height=600)

TESTA = turtle.Turtle()
TESTA.shape("square")
TESTA.color("green")
TESTA.penup()
TESTA.goto(0, 0)
TESTA.direction = "stop"

CIBO = turtle.Turtle()
CIBO.shape("circle")
CIBO.color("yellow")
CIBO.penup()
CIBO.goto(0, 100)

def muovi():

    if TESTA.direction == "up":

        Y = TESTA.ycor()

        TESTA.sety(Y + 20) 

# Left = X -20
# Down = Y -20
# Right = X +20

    if TESTA.direction == "down":

        Y = TESTA.ycor()

        TESTA.sety(Y - 20)

    if TESTA.direction == "right":

        X = TESTA.xcor()

        TESTA.setx(X + 20)

    if TESTA.direction == "left":

        X = TESTA.xcor()

        TESTA.setx(X - 20)

# != == diverso
    
def va_su():

    if TESTA.direction != "down":

        TESTA.direction = "up"

    # 1

def va_giu():

    if TESTA.direction != "up":

        TESTA.direction = "down"

    # 2

def va_destra():

    if TESTA.direction != "left":

        TESTA.direction = "right"

    # 3

def va_sinistra():

    if TESTA.direction != "right":

        TESTA.direction = "left"

    # 4


SCHERMO.listen()
SCHERMO.onkeypress(va_su, "Up")
SCHERMO.onkeypress(va_giu, "Down")
SCHERMO.onkeypress(va_destra, "Right")
SCHERMO.onkeypress(va_sinistra, "Left")

while True:
    SCHERMO.update()
    muovi()
    time.sleep(0.1)     






