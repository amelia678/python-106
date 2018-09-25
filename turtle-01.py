import turtle

painter = turtle.Turtle()

painter.pencolor('pink')

for i in range(50):
    painter.forward(50)
    painter.left(123)

painter.pencolor('purple')
for i in range(50):
    painter.forward(100)
    painter.left(123)

painter.pencolor('turquoise')
for i in range(50):
    painter.forward(200)
    painter.left(123)    

turtle.done()    
