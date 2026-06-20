import turtle
import time
import random 

CORPO = [] 
punteggio = 0
punteggio_massimo = 0

SCHERMO = turtle.Screen()
SCHERMO.title("Snake")
SCHERMO.bgcolor("black")
SCHERMO.setup(width=600, height=600)
SCHERMO.tracer(0)

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

PENNA = turtle.Turtle()
PENNA.speed(0)
PENNA.color("white")
PENNA.penup()
PENNA.hideturtle()
PENNA.goto(0, 260)
PENNA.write("Punti: 0, Record: 0", align="center", font=("Courier", 24, "normal"))

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

    if TESTA.xcor() > 290 or TESTA.xcor() < -290 or TESTA.ycor() > 290 or TESTA.ycor() < -290:
        time.sleep(1)
        TESTA.goto(0, 0)
        TESTA.direction = "stop"
        for pezzo in CORPO:
            pezzo.goto(1000, 1000)
        CORPO.clear()
        punteggio = 0
        PENNA.clear()
        PENNA.write(f"Punti: {punteggio}  Record: {punteggio_massimo}", align="center", font=("Courier", 24, "normal"))

    for indice in range(len(CORPO) - 1, 0, -1):
        X_PRECEDENTE = CORPO[indice - 1].xcor()
        Y_PRECEDENTE = CORPO[indice - 1].ycor()
        CORPO[indice].goto(X_PRECEDENTE, Y_PRECEDENTE)

    if len(CORPO) > 0:
        X_TESTA = TESTA.xcor()
        Y_TESTA = TESTA.ycor()
        CORPO[0].goto(X_TESTA, Y_TESTA)

    muovi()


    if TESTA.distance(CIBO) < 20:

        X_CASUALE = random.randint(-14, 14) * 20

        Y_CASUALE = random.randint(-14, 14) * 20
        CIBO.goto(X_CASUALE, Y_CASUALE)

    

        NUOVO_PEZZO = turtle.Turtle()
        NUOVO_PEZZO.shape("square")
        NUOVO_PEZZO.color("green")
        NUOVO_PEZZO.penup()
        CORPO.append(NUOVO_PEZZO)

        punteggio += 1
        if punteggio > punteggio_massimo:
            punteggio_massimo = punteggio
        PENNA.clear()
        PENNA.write(f"Punti: {punteggio}  Record: {punteggio_massimo}", align="center", font=("Courier", 24, "normal"))


    time.sleep(0.1)











