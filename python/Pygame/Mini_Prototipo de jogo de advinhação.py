from pygame import *
from pygame.locals import QUIT
import sys
import random

# Loop principal
init()
clock = time.Clock()
window = display.set_mode((1700, 1000))
fonte = font.Font(None, 50)
texto = fonte.render('', True, (255, 255, 255))
texto_input = ''
texto2 = fonte.render(texto_input, True, (255, 255, 255))
escolha_IA = random.randint(1,1023)
tentativas = 0
tentativas = str(tentativas)
texto_titulo = fonte.render('JOGO DA ADVINHAÇÃO, advinhe o que o bot está pensando ( um número entre 1 e 1023)', True, ('black'))
texto_tentativas = fonte.render(tentativas, True, ('black'))

#loop
while True:
    window.fill('pink')
    window.blit(texto,(200,200))
    window.blit(texto_titulo,(100,100))
    texto_tentativas = fonte.render(tentativas, True, ('black'))
    window.blit(texto_tentativas,(100,200))
    texto2 = fonte.render(texto_input, True, ('black'))
    window.blit(texto2,(300,300))
    for ev in event.get():
        
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            mouse_x, mouse_y = ev.pos
        if ev.type == KEYDOWN:
            texto_input += ev.unicode #qual botao especifico foi clicado e soma:
        if ev.type == KEYDOWN and ev.key == K_RETURN: #checa se qualquer botao foi clicado
            num = int(texto_input)
            if num == escolha_IA:
                texto = fonte.render('ACERTOU O NÚMERO', True, ('black'))
                texto_input = ''
                tentativas = str(tentativas)
                
            if num > escolha_IA:
                tentativas = int(tentativas)
                texto = fonte.render('SEU NÚMERO É MAIOR', True, ('black'))
                texto_input = ''
                tentativas += 1
                tentativas = str(tentativas)
                
            if num < escolha_IA:
                tentativas = int(tentativas)
                texto = fonte.render('SEU NÚMERO É MENOR', True, ('black'))
                texto_input = ''
                tentativas += 1
                tentativas = str(tentativas)
            
            
    
    
    


    
    
    
    
    
    
    
    
    display.update()
                    