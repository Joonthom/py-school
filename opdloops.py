from turtle import Screen, Turtle 
from random import randint

screen = Screen()      # er wordt een variabele screen gemaakt.
screen.setup(1000, 600) # de maten van het venster worden bepaald.

# Pijlicoon en snelheid
t = Turtle(visible=False) # maakt een variabele met turtle en maakt het pijlicoontje onzichtbaar
t.speed('fastest')        # zorgt dat er zo snel mogenlijk bewogen kan worden

# maak een startline en een finishlijn variabele. 
START_LINE = -300 
FINISH_LINE = 300

# teken de horizontale lijnen 
for y in range(-200, 300, 100):  # vanaf -200 op de lijn y
   t.up() 
   t.goto(START_LINE - 100, y) 
   t.down() 
   t.forward((FINISH_LINE + 90) - (START_LINE - 100))

# Starting and Finishing Gates
for x in [START_LINE - 100, FINISH_LINE - 10]:
   t.up() 
   t.goto(x,200) 
   t.right(90)
   t.down() 
   t.forward(400)
   t.left(90)
   t.forward(100)
   t.left(90)
   t.forward(400)
   t.right(90)

#Kandidaat 1
c = Turtle('turtle')
c.color('blue')
c.speed(5)
c.up()
c.goto(START_LINE -50, 50)
c.right(360)

#Kandidaat 2
c = Turtle('turtle')
c.color('blue')
c.speed(5)
c.up()
c.goto(START_LINE -50, 50)
c.right(360)