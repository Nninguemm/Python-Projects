from turtle import *
import random

#variaveis
t = Turtle()
window = Screen()
t.speed(0)
colormode(255)
window.tracer(0)

def colores1(y):
    return (0 + y,0 + y,0 + y)

def Color2():
    return random.randint(1,255), random.randint(1,255) , random.randint(1,255)

#funcoes
def trapezio(tam, i):
    t.pd()
    t.begin_fill()
    t.fillcolor(colores1(i))
    for i in range(3):
        t.fd(tam)
        t.rt(60)
    t.end_fill()
    t.pu()

def drawspiral(size,color):
    if size == 0:
        return
    trapezio(size, min(color + 3,255))
    t.lt(10)
    t.fd((size)/2)
    drawspiral(size - 1, min(color + 3,255))
    return

def star(size):
    if size < 10:
        return
    for i in range(5):
        t.fd(size)
        star(size/1.7)
        t.lt(216)

def tree(size, ang):
  #caso base
  if size < 15:
    return
  
  #1 root
  t.color(Color2())
  t.fd(size)
  t.rt(ang)
  tree(size * 0.7, ang)
  t.lt(ang)
  
  #2 root
  tree(size * 0.7, ang)
  t.lt(ang)
  

  #3root
  tree(size * 0.7, ang)
  t.rt(ang)
  t.color(Color2())
  t.bk(size)
  #fruta
  t.fillcolor('black')
  t.begin_fill()
  t.circle(1.7)
  t.end_fill()


def pentago(size):
    if size < 5:
        return
    for i in range (5):
        star(size/2.1)
        t.color(Color2())
        t.fd(size)
        pentago(size/2)
        t.lt(72)

t.pu()
t.goto(-100,0)
t.pd()  
pentago(100)
 
t.pu()
t.goto(-350,200)
t.pd()  
drawspiral(70,1)


t.pu()
t.goto(270,0)
t.pd()    
t.lt(110)  
tree(100,40)  
   
   
   
   
window.mainloop()