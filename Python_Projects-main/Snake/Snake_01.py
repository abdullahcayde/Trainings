import time
import turtle
import random

hiz = 0.2

pencere = turtle.Screen()
pencere.title('Yilan Oyunu')
pencere.bgcolor('lightblue')
pencere.setup(width=600, height=600)
pencere.tracer(0) # Guncelleme engellenir

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup() # Kafa hareket ederken yazi yazmayacak
kafa.goto(0, 100)
kafa.direction = 'stop'

yemek = turtle.Turtle()
kafa.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.90, 0.90)

def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 15)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 15)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 15)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 15)

def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'
def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'
def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'
def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

pencere.listen()   # Klavyeyi dinliyoruz
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')


kuyruklar = []

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction  ='stop'

        #Kuyruk Sifirlamak
        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

    # Kafa ve yemek arasindaki mesafe 20 pikselden az ise
    if kafa.distance(yemek) < 17:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x,y)

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed()
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)



    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i -1].xcor()
        y = kuyruklar[i -1].ycor()
        kuyruklar[i].goto(x, y)
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()
    time.sleep(hiz)

