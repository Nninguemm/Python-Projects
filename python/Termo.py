# -*- coding: utf-8 -*-
"""
Editor Spyder
 
Este é um arquivo de script temporário.
"""
import random
import sys

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


