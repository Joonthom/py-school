import turtle 
import time

s = turtle.Screen() 
s.bgcolor("blue")

number = int(input('Enter your a number: ')) 

if number < 3: 
   turtle.circle(60) 
   time.sleep(5) 

elif number >= 3 and number < 5:
   turtle.dot(20) 
   turtle.title("My yellow turtle") 
   turtle.bgcolor("yellow") 
   time.sleep(5)

elif number >= 5 and number < 7:
   turtle.shape("square")
   turtle.color('blue') 
   turtle.title("My blue turtle") 
   turtle.bgcolor("red") 
   time.sleep(5)

elif number == 8:
   turtle.shape("triangle")
   turtle.color('yellow') 
   turtle.title("My yellow turtle") 
   turtle.bgcolor("green") 
   time.sleep(5)

else:
   print("Er is iets fout gegaan")
   turtle.bgcolor("red")

#Dit als laatste lijn houden
s = turtle.getscreen()
turtle.exitonclick()