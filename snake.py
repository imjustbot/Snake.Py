import turtle
import time
import random 

CORPO = [] 

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

    TESTA.direction = "up"

    # 1

def va_giu():

    TESTA.direction = "down"

    # 2

def va_destra():

    TESTA.direction = "right"

    # 3

def va_sinistra():

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

    if TESTA.distance(CIBO) < 20:

        X_CASUALE = random.randint(-280, 280)

        Y_CASUALE = random.randint(-280, 280)
        CIBO.goto(X_CASUALE, Y_CASUALE)

    

        NUOVO_PEZZO = turtle.Turtle()
        NUOVO_PEZZO.shape("square")
        NUOVO_PEZZO.color("green")
        NUOVO_PEZZO.penup()
        CORPO.append(NUOVO_PEZZO)

    if len(CORPO) > 0:

        X_TESTA = TESTA.xcor()
        Y_TESTA = TESTA.ycor()

        CORPO[0].goto(X_TESTA, Y_TESTA)

    time.sleep(0.1)






