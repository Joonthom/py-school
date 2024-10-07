import turtle

t = turtle.Turtle()
t.speed(1)
t.pendown()

# #Square
# t.goto(0, -100)
# t.goto(-100, -100)
# t.goto(-100, 0)
# t.goto(0, 0)

# #Triangle
# t.goto(-100,100)
# t.goto(100,100)
# t.goto(0,0)
# t.home()

# #Circle met achtergrond
turtle.bgcolor("blue")
#t.circle(60)
t.dot(20)

# t = turtle.Turtle()$
# t.pendown()
# t.rt(90)
# t.fd(100)

#Dit als laatste lijn houden!!
s = turtle.getscreen()
turtle.exitonclick()