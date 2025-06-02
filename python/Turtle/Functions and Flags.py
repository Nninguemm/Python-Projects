from turtle import *
t = Turtle()

t.pu()
t.goto(-300,300)
t.pd()

def retangulovertical(x,y,tamanho1,tamanho2,cor):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
            t.fd(tamanho1)
            t.rt(90)
            t.fd(tamanho2)
            t.rt(90)
    t.end_fill()

def estrela(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4): 
        t.right(144) 
        t.forward(20)
    t.end_fill()

def triangulo(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.lt(120)
        t.fd(tamanho)
    t.end_fill()

def losango(x,y,tamanho,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.rt(150)
    for i in range(2):
        t.fd(tamanho)
        t.rt(60)
        t.fd(tamanho)
        t.rt(120)
    t.end_fill()

def retangulohorizontal(x,y,tamanho1,tamanho2,color):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(tamanho1)
        t.lt(90)
        t.fd(tamanho2)
        t.lt(90)
    t.end_fill()

def circulo(x,y,raio,color):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(raio)
    t.end_fill

def italia():
     retangulovertical(-400,300,25,50,'green')
     retangulovertical(-375,300,25,50,'white')
     retangulovertical(-350,300,25,50,'red')

def irlanda():
    t.clear()
    retangulovertical(-320,300,25,50,'green')
    retangulovertical(-295,300,25,50,'white')
    retangulovertical(-270,300,25,50,'orange')

def franca():
    t.clear()
    retangulovertical(-250,300,25,50,'blue')
    retangulovertical(-225,300,25,50,'white')
    retangulovertical(-200,300,25,50,'red')

def belgica():
    t.clear()
    retangulovertical(-70,300,25,50,'black')
    retangulovertical(-45,300,25,50,'yellow')
    retangulovertical(-20,300,25,50,'red')

def japao():
     t.clear()
     retangulohorizontal(-170,250,100,50,'white')
     t.pu()
     t.goto(-120,255)
     t.pd()
     t.fillcolor('red')
     t.begin_fill()
     t.circle(20)
     t.end_fill()

def russia():
     t.clear()
     retangulohorizontal(0,200,80,20,'white')
     retangulohorizontal(0,180,80,20,'blue')
     retangulohorizontal(0,160,80,20,'red')
   
def yemen():
     t.clear()
     retangulohorizontal(0,200,80,20,'red')
     retangulohorizontal(0,180,80,20,'white')
     retangulohorizontal(0,160,80,20,'black')

def austria():
     t.clear()
     retangulohorizontal(0,200,80,20,'red')
     retangulohorizontal(0,180,80,20,'white')
     retangulohorizontal(0,160,80,20,'red')
     
def alemanha():
     t.clear()
     retangulohorizontal(0,200,80,20,'black')
     retangulohorizontal(0,180,80,20,'red')
     retangulohorizontal(0,160,80,20,'yellow')

def hungria():
     t.clear()
     retangulohorizontal(0,200,80,20,'red')
     retangulohorizontal(0,180,80,20,'white')
     retangulohorizontal(0,160,80,20,'green')
 
def estonia():
     t.clear()
     retangulohorizontal(0,200,80,20,'blue')
     retangulohorizontal(0,180,80,20,'black')
     retangulohorizontal(0,160,80,20,'white')

def polonia():
     t.clear()
     retangulohorizontal(0,200,80,30,'white')
     retangulohorizontal(0,170,80,30,'red')

def indonesia():
     t.clear()
     retangulohorizontal(0,200,80,30,'red')
     retangulohorizontal(0,170,80,30,'white')

def ucrania():
     t.clear()
     retangulohorizontal(0,200,80,30,'blue')
     retangulohorizontal(0,170,80,30,'yellow')

def brasil():
     t.clear()
     retangulohorizontal(0,0,200,100,'green')
     losango(185,50,100,'yellow')
     t.penup()
     t.goto(85,70)
     t.pendown()
     t.color("blue")
     t.begin_fill()
     t.circle(25)
     t.end_fill()
     t.rt(210)
     retangulohorizontal(74,45,50,10,'white')
        
def cuba():
    t.clear()
    retangulohorizontal(0,0,80,10,'blue')
    retangulohorizontal(0,-10,80,10,'white')
    retangulohorizontal(0,-20,80,10,'blue')
    retangulohorizontal(0,-30,80,10,'white')
    retangulohorizontal(0,-40,80,10,'blue')
    t.rt(90)
    triangulo(0,-40,50,'red')
    t.rt(180)
    t.fd(30)
    t.rt(90)
    t.pu()
    t.fd(30)
    t.pd()
    estrela('white')
    t.right(144)
    t.rt(90)

def palestina():
     t.clear()
     t.lt(90)
     retangulohorizontal(0,200,80,20,'black')
     retangulohorizontal(0,180,80,20,'white')
     retangulohorizontal(0,160,80,20,'green')
     t.rt(90)
     triangulo(0,160,60,'red')

def bahamas():
     t.clear()
     t.lt(90)
     retangulohorizontal(0,200,80,20,'cyan')
     retangulohorizontal(0,180,80,20,'yellow')
     retangulohorizontal(0,160,80,20,'cyan')
     t.rt(90)
     triangulo(0,160,60,'black')

italia()
irlanda()
franca()
belgica()
japao()
russia()
yemen()
austria()
alemanha()
hungria()
estonia()
polonia()
indonesia()
ucrania()
brasil()
cuba()
palestina()
bahamas()



            

    


     




























window = Screen()
window.mainloop()