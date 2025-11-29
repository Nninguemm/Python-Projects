from turtle import *
import time
import math

t = Turtle()
t2 = Turtle()
t.speed(0)

def plano():
    t2.fd(400)
    t2.stamp()
    t2.bk(400)
    t2.rt(90)
    t2.fd(400)
    t2.rt(180)
    t2.fd(800)
    t2.stamp()
    t2.rt(180)
    t2.fd(400)
    t2.lt(90)
    t2.bk(400)

def fun1(x):
    return x**0.5

def fun2(x):
    return 1/x


def fun3(x):
    return 2**x

def fun4(x):
    return 5 - x**2

def fun5(x):
    return x**2 - 5*x + 6

def fun6(x):
    return x**3 - x*2 - x + 1

plano()

t.color('red')
limite_x_sup = 100
limite_x_inf = 0
t.pu()
t.goto(limite_x_inf, fun1(limite_x_inf))
t.pd()
for x in range(limite_x_inf,limite_x_sup):
    y = fun1(x)
    t.goto(x*5,y)



t.clear()
t.color('blue')  
t.speed(0)
limite_x_inf = -100
limite_x_sup = 0
t.pu()
for x in range(limite_x_inf, limite_x_sup):
    if x == 0:
        continue  
    y = fun2(x)
    t.goto(x * 10, y * 100) 
    t.pd()

limite_x_inf = 0
limite_x_sup = 100
t.pu()
for x in range(limite_x_inf, limite_x_sup):
    if x == 0:
        continue  
    y = fun2(x)
    t.goto(x * 10, y * 100) 
    t.pd()







t.pu()
t.clear()
t.color('cyan')
limite_x_sup = 50
limite_x_inf = -100
t.pd()
t.pu()
t.goto(limite_x_inf, fun3(limite_x_inf))
t.pd()
for x in range(limite_x_inf,limite_x_sup):
    y = fun3(x)
    t.goto(x*10,y)


t.clear()
t.color('purple')
limite_x_sup = 40
limite_x_inf = -100
t.pu()
t.goto(limite_x_inf, fun4(limite_x_inf))
t.pd()
for x in range(limite_x_inf,limite_x_sup):
    y = fun4(x)
    t.goto(x*4,y)

t.clear()
limite_x_sup = 40
limite_x_inf = -100
t.pu()
t.goto(limite_x_inf, fun5(limite_x_inf))
t.pd()
for x in range(limite_x_inf,limite_x_sup):
    y = fun5(x)
    t.goto(x*10,y)

t.clear()
t.color('pink')
limite_x_sup = 20
limite_x_inf = -100
t.pu()
t.goto(limite_x_inf, fun6(limite_x_inf))
t.pd()
for x in range(limite_x_inf,limite_x_sup):
    y = fun6(x)
    t.goto(x*10,y)









 





window = Screen()
window.mainloop()