from turtle import *

#cria a tartaruga
t = Turtle()
for i in range(5):
    t.fd(60)
    t.rt(30)
    t.fd(70)
    t.lt(60)
    t.fd(70)
    t.rt(30)
    t.fd(70)
    t.lt(72)


#abrir e manter a janela
window = Screen()
window.mainloop()