# setup!
import turtle 

t = turtle.Turtle()
# where to go and other colors for it
t.goto(-100,0)
t.color("cyan")
turtle.Screen().bgcolor("black")
t.speed(10)

# making the art
colors = ["pink","yellow","orange"]
for i in range(1000):
    t.color( colors[ i %3])
    t.forward(400)
    t.left(201)



turtle.exitonclick()