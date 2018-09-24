from turtle import *

def center_turtle():
  up()
  forward(50)
  left(90)
  forward(50)
  left(270)

  down()



def draw_circle():
  begin_fill()
  fillcolor('black')
  pencolor('black')
  width(10)
  circle(180)
  end_fill()

draw_circle()
input()
