from turtle import *

#cria a tartaruga
t = Turtle()

t.color
t.fd(200)
t.bk(200)
t.rt(90)
t.fd(200)
t.rt(180)
t.fd(400)
t.rt(180)
t.fd(200)
t.lt(90)
t.bk(200)

t.penup()
t.goto(-180,20)
t.pd()
color = textinput("solicitar a cor", "digite a cor")
t.color("blue")
t.fillcolor(color)
t.begin_fill()
for i in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

t.penup()
t.goto(180,20)
t.pd()
color = textinput("solicitar a cor", "digite a cor")
t.color("pink")
t.fillcolor(color)
t.begin_fill()
for i in range(5):
    t.lt(72)
    t.fd(100)
t.end_fill()

t.penup()
t.goto(-180,-20)
t.pd()
color = textinput("solicitar a cor", "digite a cor")
t.color("red")
t.fillcolor(color)
t.begin_fill()
t.fd(40)
for i in range (9):
    t.rt(36)
    t.fd(40)
t.end_fill()

t.penup()
t.goto(180,-20)
t.pd()
color = textinput("solicitar a cor", "digite a cor")
t.color("black")
t.fillcolor(color)
t.begin_fill()
t.rt(96)
for i in range(6):
    t.fd(50)
    t.rt(60)
t.end_fill()

t.speed(0)
t.penup()
t.goto(-50, 50)
t.pd()
t.color("blue")
for i in range(20):
    t.fd(2)
    t.rt(10)
for i in range(20):
    t.fd(4)
    t.rt(10)
for i in range(20):
    t.fd(6)
    t.rt(10)
for i in range(20):
    t.fd(8)
    t.rt(10)
    
























#abrir e manter a janela
window = Screen()
window.mainloop()