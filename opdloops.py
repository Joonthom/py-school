import turtle
from turtle import Screen, Turtle 
from random import randint

screen = Screen()
screen.setup(1000, 600) 

# Pijlicoon en snelheid
t = Turtle(visible=False)
t.speed('fastest')        

# maakt een startline en een finishlijn variabele. 
START_LINE = -300 
FINISH_LINE = 300

# teken de horizontale lijnen 
for y in range(-200, 300, 100):
   t.up() 
   t.goto(START_LINE - 100, y) 
   t.down() 
   t.forward((FINISH_LINE + 90) - (START_LINE - 100))

# Start en Finishgates
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

# Kandidaat 1
d = Turtle('turtle')
d.color('red')
d.speed(5)
d.up()
d.goto(START_LINE -50, 150)
d.right(360)

# Kandidaat 2
c = Turtle('turtle')
c.color('blue')
c.speed(5)
c.up()
c.goto(START_LINE -50, 50)
c.right(360)

# Kandidaat 3
b = Turtle('turtle')
b.color('yellow')
b.speed(5)
b.up()
b.goto(START_LINE -50, -50)
b.right(360)

# Kandidaat 4
a = Turtle('turtle')
a.color('green')
a.speed(5)
a.up()
a.goto(START_LINE -50, -150)
a.right(360)

# while loop die er voor zorgt dat ze stoppen zodra de eerste over de finish is.
while a.xcor() < FINISH_LINE and b.xcor() < FINISH_LINE and c.xcor() < FINISH_LINE and a.xcor() < FINISH_LINE:
   a.forward(randint(1, 6))
   b.forward(randint(1, 6))
   c.forward(randint(1, 6))
   d.forward(randint(1, 6))
screen.mainloop()

# Dit als laatste lijn houden
s = turtle.getscreen()
turtle.exitonclick()