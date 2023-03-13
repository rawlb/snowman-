"""
when I made the snowman I was not awair of the specks on canvis so i just made one. 
"""
# lines 1-7 will define variables and set up code.
circle=100
color=("lightblue")
import turtle 
turtle.showturtle()
turtle.speed(1/2)
turtle.penup()
# lines 8-28 manke the three snowballs for the snowman.
turtle.goto(-0,-100)
turtle.pendown
turtle.right(180)
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.circle(circle)
turtle.end_fill()
turtle.goto(0,-115)
turtle.right(180) 
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.circle(circle-25)
turtle.end_fill()
turtle.right(-90)
turtle.goto(0,10)
turtle.begin_fill()
turtle.right(90)
turtle.fillcolor("lightblue")
turtle.circle(circle-50)
turtle.end_fill()
# lines 29-39 will make the eyes.
turtle.goto(20,70)
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(5)
turtle.end_fill()
turtle.goto(-20,70)
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(5)
turtle.end_fill()
# lines 41-45 will make the snowmans' the mouth
turtle.pensize(10)
turtle.penup()
turtle.goto(-15,40)
turtle.pendown()
turtle.forward(30)
# lines 47-56 will make the hat.
turtle.pensize(12)
turtle.penup()
turtle.goto(-40,90)
turtle.pendown()
turtle.forward(80)
turtle.left(180)
turtle.forward(10)
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(30,180) #semicircle
turtle.end_fill()
# lines 60-71 will makes the tie
turtle.penup()
turtle.goto(-35,20)
turtle.pendown()
turtle.left(50)
turtle.circle(60,75)
turtle.pensize(20)
turtle.pencolor("red")
turtle.penup()
turtle.goto(0,10)
turtle.pendown()
turtle.right(125)
turtle.forward(100)
# lines 73-86 will make the firest arm and finger.
turtle.penup()
turtle.goto(-60,-4)
turtle.right(90)
turtle.pencolor("brown")
turtle.pendown()
turtle.pensize(22)
turtle.forward(100)
#this makes the fingers.
turtle.right(45)
turtle.pensize(15)
for i in range(3):
    turtle.left(30)
    turtle.forward(60)
    turtle.backward(60)
 #lines 88-102 will make the other arm and fingers.
turtle.right(89)
turtle.penup()
turtle.goto(60,-4)
turtle.right(90)
turtle.pencolor("brown")
turtle.pendown()
turtle.pensize(22)
turtle.forward(100)
#fingers.
turtle.pensize(15)
turtle.right(45)
for i in range(3):
    turtle.left(30)
    turtle.forward(60)
    turtle.backward(60)







input("press enter to exit")


 
