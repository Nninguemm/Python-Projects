from turtle import *

#cria a tartaruga

speed(300)
fillcolor('red')
begin_fill()
lt(30)
fd(75)
for p in range(200):
    lt(1)
    fd(1)
pu()
goto(0,0)
pd()
rt(72.5)
fd(75)
for p in range(200):
    rt(1)
    fd(1)
end_fill()










window = Screen()
window.mainloop()