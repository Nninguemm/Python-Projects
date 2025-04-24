# -*- coding: utf-8 -*-
"""
Editor Spyder
 
Este é um arquivo de script temporário.
"""
import random
import sys
import tkinter as tk

y = -1
def o_jogo():
    if  a[0] == palavra_chave[0]:
        print('a primeira letra está correta')
    elif a[0] in palavra_chave:
        print('a primeira letra está na posição incorreta')
    else:
        print('a primeira letra está incorreta')

    if  a[1] == palavra_chave[1]:
        print('a segunda letra está correta')
    elif a[1] in palavra_chave:
        print('a segunda letra está na posição incorreta')
    else:
        print('a segunda letra está incorreta')
 
    if  a[2] == palavra_chave[2]:
        print('a terceira letra está correta')
    elif a[2] in palavra_chave:
        print('a terceira letra está na posição incorreta')
    else:
        print('a terceira letra está incorreta')
  
    if  a[3] == palavra_chave[3]:
        print('a quarta letra está correta')
    elif a[3] in palavra_chave:
        print('a quarta letra está na posição incorreta')
    else:
        print('a quarta letra está incorreta')
  
    if  a[4] == palavra_chave[4]:
        print('a quinta letra está correta')
    elif a[4] in palavra_chave:
        print('a quinta letra está na posição incorreta')
    else:
        print('a quinta letra está incorreta')
    
    if a == palavra_chave:
        print('parabens, voce acertou a palavra!!!!!') 
        sys.exit()
        

# Create the main window
tela = tk.Tk()
tela.title("jogo")
tela.geometry("1200x800")  # width x height

# Add widgets (optional)
label = tk.Label(tela, text="Vamos jogar termo? clique em iniciar", font = ('Arial',30), fg="blue")
label.pack(pady=10)
label.place(x=250,y=100)

def tela2():
    tela_jogo = tk.Tk()
    tela_jogo.geometry("1200x800")
    text1 = tk.Label(tela_jogo, text='escolha uma palavra de 5 letras',font = ('Arial',30), fg="blue",).grid(row=0)
    tk.Entry(tela_jogo)
    tela_jogo.mainloop()

button = tk.Button(tela, text="iniciar", width = 5, height = 2,font = ('Arial',50,), fg="red",bg="green",command=lambda: tela2())
button.pack()
button.place(x=500,y=300,)


# Run the application
tela.mainloop()


a = input('voce tem apenas 4 tentativas\nescolha uma palavra de 5 letras:')
lista = ['sagaz','termo','mexer','nobre','senso','afeto','poder','sonho','amigo','morra','audio,','gamer','cinco']
palavra_chave = random.choice(lista)
list(a)
list(palavra_chave)
x = 4
while x > 1:
    o_jogo()
    print('\nproxima tentativa')
    x = x-1
    a = input(f'voce tem apenas {x} tentativas\nescolha uma palavra de 5 letras:')
o_jogo()
print('OTARIO VC PERDEU')


   

