import turtle


painter = turtle.Turtle()

painter.pencolor('orange')

for i in range(50):
    painter.forward(200)
    painter.left(123)

painter.pencolor('pink')
for i in range(50):
    painter.forward(300)
    painter.left(123)

painter.pencolor('turquoise')
for i in range(50):
    painter.forward(400)
    painter.left(123)    

turtle.done()    
