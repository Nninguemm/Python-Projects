from pygame import *
from pygame.locals import QUIT
import sys
import random

def desenhar_menu():
    window.fill('black')
    draw.rect(window, 'blue', (300, 350, 270, 80))
    draw.rect(window, 'blue', (800, 350, 270, 80))
    draw.rect(window, 'blue', (1290, 350, 270, 80))
    fonte = font.Font(None, 30)
    texto = fonte.render('PEDRA,PAPEL,TESOURA', True, (255, 255, 255))
    window.blit(texto, (310, 360))
    fonte = font.Font(None, 80)
    texto = fonte.render('Escolha um jogo:', True, (255, 255, 255))
    window.blit(texto, (500, 100))
    fonte = font.Font(None, 30)
    texto = fonte.render('TERMO', True, (255, 255, 255))
    window.blit(texto, (810, 360))
    texto = fonte.render('CALCULADORA', True, (255, 255, 255))
    window.blit(texto, (1300, 360))


def login():
    window.fill('grey')
    fonte = font.Font(None, 50)
    texto = fonte.render('Digite seu login (email e senha) nas caixas de texto verdes:', True, (255, 255, 255))
    window.blit(texto, (400, 100))
    draw.rect(window, 'green', (450, 250, 700, 80))
    draw.rect(window, 'green', (450, 360, 700, 80))
    draw.rect(window, 'black', (650, 500, 270, 80))
    texto = fonte.render('ENTER', True, (255, 255, 255))
    window.blit(texto, (720, 520))
    

#criar função para ver se o email é válido
def valida_email(email):
    sufix = email[-8:]
    if sufix == '@puc.com':
        return True
    return False

#criar função para ver se o email é válido só que melhor (função booleana)
def valida_email_2(email):
    return email[-8:] == '@puc.com'

#criar função para ver se a senha é válido
def valida_senha(senha):
    if len(senha) < 8: #early return, deixa o código mais limpo (nesse caso ve se a senha nao condiz em vez de se vale)
        return False
    cont_maiusc = 0
    cont_minusc = 0
    cont_num = 0
    for char in senha:
        if 'A' <= char <= 'Z': #verifica se tem algum caracter maiusculo
            cont_maiusc += 1
        if 'a' <= char <= 'z': #verifica se tem algum caracter minusculo
            cont_minusc += 1
        if '0' <= char <= '9': #verifica se tem alguma letra
            cont_num += 1

    if cont_maiusc == 0: # nao tem nenhum caracter maiusculo, return falso, senha invalida
        return False
    if cont_minusc == 0: # nao tem nenhum caracter minusculo, return falso, senha invalida
        return False
    if cont_num == 0: # nao tem nenhuma nenhuma, return falso, senha invalida
        return False
    
    return True # senha válida

def criptografa(senha): # cripotografa a senha em cifra de césar
    senha_cript = ''
    posASCII = ''
    for char in senha:
        if 'a' <= char <= 'z':  # cripotografa as letras maiusculas em cifra de césar and posASCII = caracter final criptografado
            posASCII = ord(char) # pega o valor da letra
            posASCII -= ord('a') # diminui o valor com a minuscula com menor valor
            posASCII += 3 #soma 3 no valor (a parte do cifra de césar em si, em que cada caracter vira outro +3 para frente (como o 'a' vira 'd'))
            posASCII = ord('a') + (posASCII)%26 # soma o valor com a minuscula com menor valor para voltar com a letra correta mas faz (posASCII)%26 para garantir que x,y,z retornem os valores a,b,c e não continuem somando somando para outros carcteres (exemplo x: 120-97 = 23, 23 + 3 = 26, ord(a) + 26%26(=0) = valor de a)
            senha_cript += chr(posASCII) #tranforma o valor do caracter incriptado correto em letra e o soma na senha incriptada
            
        elif 'A' <= char <= 'Z':  # cripotografa as letras maiusculas em cifra de césar, posASCII = caracter final criptografado
            posASCII = ord(char) # pega o valor da letra
            posASCII -= ord('A') # diminui o valor com a maiuscula com menor valor
            posASCII += 3 #soma 3 no valor (a parte do cifra de césar em si, em que cada caracter vira outro +3 para frente (como o 'A' vira 'D'))
            posASCII = ord('A') + (posASCII)%26  # soma o valor com a maiuscula com menor valor para voltar com a letra correta mas faz (posASCII)%26 para garantir que X,Y,Z retornem os valores A,B,C e não continuem somando para outros carcteres (exemplo Z: 90 - 65 = 25, 25 + 3 = 28, ord(A) + 28%26(=2) = valor de a + 3 = valor de c )
            senha_cript += chr(posASCII) #tranforma o valor do caracter incriptado correto em letra e o soma na senha incriptada
            
        elif '0' <= char <= '9':  # cripotografa os números em cifra de césar posASCII = caracter final criptografado
            posASCII = ord(char) # pega o valor do numero
            posASCII -= ord('0') # diminui o valor com o número de menor valor
            posASCII += 3 #soma 3 no valor (a parte do cifra de césar em si, em que cada caracter vira outro +3 para frente (como o '0' vira '3'))
            posASCII = ord('0') + (posASCII)%10 # soma o valor com o número com menor valor para voltar com o número correta mas faz (posASCII)%10 para garantir que 7,8,9 retornem os valores 0,1,2 e não continuem somando para outros carcteres (exemplo 8: 56 - 48 = 8, 8 + 3 = 11, ord(0) + 11%10(=1) = valor de 0 + 1 = valor de 1)
            senha_cript += chr(posASCII) #tranforma o valor do caracter incriptado correto em numero e o soma na senha incriptada
            
        else:
            senha_cript += char
    print(senha_cript)
            
            
            
            
            


#para a calculadora
def texto_voumematar(t, x, y):
    img = fonte_global.render(t, True, (255, 255, 255))
    window.blit(img, (x, y))


init()
clock = time.Clock()
window = display.set_mode((1700, 1000))
display.set_caption("Login e jogos")
fonte = font.Font(None, 40)

#login variaveis
pre_email = ''
pre_senha = ''
email = ''
senha = ''
texto_email = fonte.render(pre_email, True, 'red')
texto_senha = fonte.render(pre_senha, True, 'red')
modo = ''
senh_c = ''

textinho1 = ''
textinho = fonte.render(textinho1,True,'red')




# Estados da tela
MENU = "menu"
JOGO = "jogo"
JOGO2 = 'jogo2'
JOGO3 = 'jogo3'
LOGIN = 'login'
estado_tela = LOGIN

#JOGO1
wins = 0
a = 0

#termo
texto_input = ''
lista = ['sagaz','termo','mexer','nobre','senso','afeto','poder','sonho','amigo','morra','audio,','gamer','cinco']
palavra_chave = random.choice(lista)
list(palavra_chave)
draw.rect(window,'grey',(400,200,80,80))
draw.rect(window,'grey',(490,200,80,80))
draw.rect(window,'grey',(580,200,80,80))
draw.rect(window,'grey',(670,200,80,80))
draw.rect(window,'grey',(760,200,80,80))
tentativa = 0
texto_final1 = fonte.render('',True,('black'))
texto3 = fonte.render('',True,(168, 50, 157))
texto4 = fonte.render('',True,(168, 50, 157))
texto5 = fonte.render('',True,(168, 50, 157))
texto6 = fonte.render('',True,(168, 50, 157))
texto7= fonte.render('',True,(168, 50, 157))
texto8 = fonte.render('',True,(168, 50, 157))
texto9 = fonte.render('',True,(168, 50, 157))
texto10 = fonte.render('',True,(168, 50, 157))
texto11 = fonte.render('',True,(168, 50, 157))
texto12= fonte.render('',True,(168, 50, 157))
texto13 = fonte.render('',True,(168, 50, 157))
texto14 = fonte.render('',True,(168, 50, 157))
texto15 = fonte.render('',True,(168, 50, 157))
texto16 = fonte.render('',True,(168, 50, 157))
texto17= fonte.render('',True,(168, 50, 157))
texto18 = fonte.render('',True,(168, 50, 157))
texto19 = fonte.render('',True,(168, 50, 157))
texto20 = fonte.render('',True,(168, 50, 157))
texto21 = fonte.render('',True,(168, 50, 157))
texto22= fonte.render('',True,(168, 50, 157))
textoa = fonte.render('',True,(168, 50, 157))
textob = fonte.render('',True,(168, 50, 157))
textoc = fonte.render('',True,(168, 50, 157))
textod = fonte.render('',True,(168, 50, 157))
textoe = fonte.render('',True,(168, 50, 157))
buttao = fonte.render('REINICIAR',True,('black'))
color= 'grey'
color1 = 'grey'
color2 = 'grey'
color3 = 'grey'
color4 = 'grey'
color6= 'grey'
color7 = 'grey'
color8 = 'grey'
color9 = 'grey'
color10 = 'grey'
color11 = 'grey'
color12 = 'grey'
color13 = 'grey'
color14 = 'grey'
color15 = 'grey'
color16= 'grey'
color17 = 'grey'
color18 = 'grey'
color19 = 'grey'
color20 = 'grey'
color21 = 'grey'
color22 = 'grey'
color23 = 'grey'
color24 = 'grey'
color25 = 'grey'

#JOGO3
fonte_global = font.Font(None, 40)
textt = ''
text_result = fonte_global.render(textt, True, ('red'))


while True:
    clock.tick(60)
    keys = key.get_pressed()
    mouse_x, mouse_y= mouse.get_pos()
    buttons = mouse.get_pressed()
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            mouse_x, mouse_y = ev.pos
            if estado_tela == MENU:
                if 300 <= mouse_x <= 570 and 350 <= mouse_y <= 430:
                    estado_tela = JOGO
                if 800 <= mouse_x <= 1070 and 350 <= mouse_y <= 430:
                    estado_tela = JOGO2
                if 1290 <= mouse_x <= 1560 and 350 <= mouse_y <= 430:
                    estado_tela = JOGO3
                    
            elif estado_tela == LOGIN:
                if (450 <= mouse_x <= 1170) and (250 <= mouse_y <= 330):
                    modo = 'email'
                elif (450 <= mouse_x <= 1170) and (360 <= mouse_y <= 420):
                    modo = 'senha'
                elif (650 <= mouse_x <= 920) and (500 <= mouse_y <= 580):
                    modo = 'cript'
                    email = pre_email
                    senha = pre_senha
                    if valida_email_2(email) == True and valida_senha(senha) == True:
                        criptografa(pre_senha)
                        estado_tela = MENU
                    else:
                        textinho1 = 'EMAIL E/OU SENHA INVALIDOS'
                        
                    
                    
        if estado_tela == LOGIN and ev.type == KEYDOWN:
            if modo == 'email':
                if ev.key == K_BACKSPACE:
                    pre_email = pre_email[:-1]
                else:
                    pre_email += ev.unicode
                texto_email = fonte.render(pre_email, True, (0, 0, 0))
            
            elif modo == 'senha':
                if ev.key == K_BACKSPACE:
                    pre_senha = pre_senha[:-1]
                else:
                    pre_senha += ev.unicode
                texto_senha = fonte.render(pre_senha, True, (0, 0, 0))


    
                


    if estado_tela == LOGIN:
        login()
        texto_email = fonte.render(pre_email, True, 'red')
        texto_senha = fonte.render(pre_senha, True, 'red')
        window.blit(texto_email,(455,260))
        window.blit(texto_senha,(455,370))
        textinho = fonte.render(textinho1,True,'red')
        window.blit(textinho,(500,200))



    #menu
    if estado_tela == MENU:
        desenhar_menu()


    #pedra,papel,tesoura    
    if estado_tela == JOGO:
        if a == 1:
            desenhar_menu()
            estado_tela = MENU
            if 300 <= mouse_x <= 570 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO
            if 800 <= mouse_x <= 1070 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO2
            if 1290 <= mouse_x <= 1560 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO3

        else:
            window.fill('pink')
            #imagens da pedra,papel e tesoura
            tesoura = image.load('tesoura.webp')
            tesoura = transform.scale(tesoura,(300,300))
            window.blit(tesoura,(200,700))
            pedra = image.load('pedra.webp')
            pedra = transform.scale(pedra,(300,300))
            window.blit(pedra,(600,700))
            papel = image.load('papel.png')
            papel = transform.scale(papel,(300,300))
            window.blit(papel,(1000,700))
            fonte = font.Font(None,40)
            texto = fonte.render('Escolha entre Pedra,Papel ou Tesoura',True,(168, 50, 157))
            window.blit(texto,(450,100))
            
            #contador de vitória
            str(wins)
            vito = 'VITÓRIAS:' + str(wins) 
            texto = fonte.render(vito,True,(168, 50, 157))
            window.blit(texto,(600,50))
            
            #IA escolhe uma opção
            tipo_jogada = [pedra,papel,tesoura]
            escolha_IA = random.choice(tipo_jogada)
            jogada_jogador = 0
            
            #butao de reiniciar
            draw.rect(window,'white',(1000,350,200,100))
            texto = fonte.render('Reiniciar',True,(168, 50, 157))
            window.blit(texto,(1020,370))
            draw.rect(window,'white',(1400,350,200,100))
            texto = fonte.render('MENU',True,(168, 50, 157))
            window.blit(texto,(1420,370))

            #Botãos de cada jogada
            mouse_x, mouse_y= mouse.get_pos()
            buttons = mouse.get_pressed()
            for ev in event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == 1:  # Botão esquerdo do mouse
                        if (1000 <= mouse_x <= 1200) and (350 <= mouse_y <= 450):
                            wins = 0
                        if (1400 <= mouse_x <= 1600) and (350 <= mouse_y <= 450):
                            estado_tela = MENU
                            a = 1
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == 1:  # Botão esquerdo do mouse
                        if (200 <= mouse_x <= 500) and (700 <= mouse_y <= 1000):
                            jogada_jogador = tesoura
                        elif (600 <= mouse_x <= 900) and (700 <= mouse_y <= 1000):
                            jogada_jogador = pedra
                        elif (1000 <= mouse_x <= 1300) and (700 <= mouse_y <= 1000):
                            jogada_jogador = papel
                        
                    #empate 
                    if escolha_IA == jogada_jogador:
                        texto = fonte.render('EMPATE',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        
                        
                    #derrotas
                    elif escolha_IA == pedra and jogada_jogador == tesoura:
                        texto = fonte.render('Perdeu',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        
                    elif escolha_IA == tesoura and jogada_jogador == papel:
                        texto = fonte.render('Perdeu',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        
                    elif escolha_IA == papel and jogada_jogador == pedra:
                        texto = fonte.render('Perdeu',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        
                    
                    #vitorias
                    elif escolha_IA == pedra and jogada_jogador == papel:
                        texto = fonte.render('Ganhou',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        int(wins)
                        wins += 1
                        str(wins)
                        
                        
                    elif escolha_IA == papel and jogada_jogador == tesoura:
                        texto = fonte.render('ganhou',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        int(wins)
                        wins += 1
                        str(wins)
                        
                    elif escolha_IA == tesoura and jogada_jogador == pedra:
                        texto = fonte.render('ganhou',True,(168, 50, 157))
                        window.blit(texto,(400,260))
                        window.blit(escolha_IA,(500,250))
                        window.blit(jogada_jogador,(100,250))
                        display.update()
                        time.delay(2000)
                        int(wins)
                        wins += 1
                        str(wins)
                
    #termo
    if estado_tela == JOGO2:
        if a == 1:
            desenhar_menu()
            estado_tela = MENU
            if 300 <= mouse_x <= 570 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO
            if 800 <= mouse_x <= 1070 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO2
            if 1290 <= mouse_x <= 1560 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO3
                
                
        else:    
            clock = time.Clock()
            clock.tick(120)
            #mouse e teclado
            keys = key.get_pressed()
            mouse_x, mouse_y= mouse.get_pos()
            buttons = mouse.get_pressed()
            window.fill('pink')
            fonte = font.Font(None,80)
            texto = fonte.render('Escolha uma palavra de 5 letras',True,(168, 50, 157))
            window.blit(texto,(350,50))
            fonte = font.Font(None,40)
            texto = fonte.render('PALAVRA:',True,(168, 50, 157))
            
            draw.rect(window,'white',(1000,550,200,100))
            textov = fonte.render('MENU',True,(168, 50, 157))
            window.blit(textov,(1010,570))
            
            draw.rect(window,'blue',(400,660,80,80))
            textom = fonte.render('= Acertou a letra',True,(168, 50, 157))
            window.blit(textom,(490,670))
            draw.rect(window,'yellow',(400,760,80,80))
            textom = fonte.render('= A letra está na posição errada',True,(168, 50, 157))
            window.blit(textom,(490,770))
            draw.rect(window,'red',(400,860,80,80))
            textom = fonte.render('= A letra está errada',True,(168, 50, 157))
            window.blit(textom,(490,870))
            
            

            
            draw.rect(window,color,(400,200,80,80))
            draw.rect(window,color1,(490,200,80,80))
            draw.rect(window,color2,(580,200,80,80))
            draw.rect(window,color3,(670,200,80,80))
            draw.rect(window,color4,(760,200,80,80))
            
            draw.rect(window,color6,(400,290,80,80))
            draw.rect(window,color7,(490,290,80,80))
            draw.rect(window,color8,(580,290,80,80))
            draw.rect(window,color9,(670,290,80,80))
            draw.rect(window,color10,(760,290,80,80))
            
            draw.rect(window,color11,(400,380,80,80))
            draw.rect(window,color12,(490,380,80,80))
            draw.rect(window,color13,(580,380,80,80))
            draw.rect(window,color14,(670,380,80,80))
            draw.rect(window,color15,(760,380,80,80))
            
            draw.rect(window,color16,(400,470,80,80))
            draw.rect(window,color17,(490,470,80,80))
            draw.rect(window,color18,(580,470,80,80))
            draw.rect(window,color19,(670,470,80,80))
            draw.rect(window,color20,(760,470,80,80))
            
            draw.rect(window,color21,(400,560,80,80))
            draw.rect(window,color22,(490,560,80,80))
            draw.rect(window,color23,(580,560,80,80))
            draw.rect(window,color24,(670,560,80,80))
            draw.rect(window,color25,(760,560,80,80))
            
            draw.rect(window,'red',(1000,200,200,120))
            window.blit(buttao,(1020,220))
            
            
            window.blit(texto,(560,150))
            window.blit(texto3,(400,200))
            window.blit(texto4,(490,200))
            window.blit(texto5,(580,200))
            window.blit(texto6,(670,200))
            window.blit(texto7,(760,200))
            
            window.blit(texto8,(400,290))
            window.blit(texto9,(490,290))
            window.blit(texto10,(580,290))
            window.blit(texto11,(670,290))
            window.blit(texto12,(760,290))
            
            window.blit(texto13,(400,380))
            window.blit(texto14,(490,380))
            window.blit(texto15,(580,380))
            window.blit(texto16,(670,380))
            window.blit(texto17,(760,380))
            
            window.blit(texto18,(400,470))
            window.blit(texto19,(490,470))
            window.blit(texto20,(580,470))
            window.blit(texto21,(670,470))
            window.blit(texto22,(760,470))
            
            window.blit(textoa,(400,560))
            window.blit(textob,(490,560))
            window.blit(textoc,(580,560))
            window.blit(textod,(670,560))
            window.blit(textoe,(760,560))
            
            window.blit(texto_final1,(900,400))
            
            
            
            for ev in event.get():
                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    if (1000 <= mouse_x <= 1200) and (550 <= mouse_y <= 650):
                        estado_tela = MENU
                        a = 1
                if ev.type == MOUSEBUTTONDOWN and ev.button == 1 and 1000 <= mouse_x <= 1200 and 200<=mouse_y<=320:
                    palavra_chave = random.choice(lista)
                    list(palavra_chave)
                    tentativa = 0
                    texto_final1 = fonte.render('',True,(168, 50, 157))
                    texto3 = fonte.render('',True,(168, 50, 157))
                    texto4 = fonte.render('',True,(168, 50, 157))
                    texto5 = fonte.render('',True,(168, 50, 157))
                    texto6 = fonte.render('',True,(168, 50, 157))
                    texto7= fonte.render('',True,(168, 50, 157))

                    texto8 = fonte.render('',True,(168, 50, 157))
                    texto9 = fonte.render('',True,(168, 50, 157))
                    texto10 = fonte.render('',True,(168, 50, 157))
                    texto11 = fonte.render('',True,(168, 50, 157))
                    texto12= fonte.render('',True,(168, 50, 157))

                    texto13 = fonte.render('',True,(168, 50, 157))
                    texto14 = fonte.render('',True,(168, 50, 157))
                    texto15 = fonte.render('',True,(168, 50, 157))
                    texto16 = fonte.render('',True,(168, 50, 157))
                    texto17= fonte.render('',True,(168, 50, 157))

                    texto18 = fonte.render('',True,(168, 50, 157))
                    texto19 = fonte.render('',True,(168, 50, 157))
                    texto20 = fonte.render('',True,(168, 50, 157))
                    texto21 = fonte.render('',True,(168, 50, 157))
                    texto22= fonte.render('',True,(168, 50, 157))

                    textoa = fonte.render('',True,(168, 50, 157))
                    textob = fonte.render('',True,(168, 50, 157))
                    textoc = fonte.render('',True,(168, 50, 157))
                    textod = fonte.render('',True,(168, 50, 157))
                    textoe = fonte.render('',True,(168, 50, 157))

                    color= 'grey'
                    color1 = 'grey'
                    color2 = 'grey'
                    color3 = 'grey'
                    color4 = 'grey'

                    color6= 'grey'
                    color7 = 'grey'
                    color8 = 'grey'
                    color9 = 'grey'
                    color10 = 'grey'

                    color11 = 'grey'
                    color12 = 'grey'
                    color13 = 'grey'
                    color14 = 'grey'
                    color15 = 'grey'

                    color16= 'grey'
                    color17 = 'grey'
                    color18 = 'grey'
                    color19 = 'grey'
                    color20 = 'grey'

                    color21 = 'grey'
                    color22 = 'grey'
                    color23 = 'grey'
                    color24 = 'grey'
                    color25 = 'grey'
                
                if ev.type == KEYDOWN and tentativa == 0 and ev.key == K_RETURN: #checa se qualquer botao foi clicado
                        list(texto_input)
                        if texto_input == palavra_chave:
                            texto_final1 = fonte.render('VOCE ACERTOU A PALAVRA!!!!',True,('black'))
                        fonte = font.Font(None,40)
                        texto3 = fonte.render(texto_input[0],True,(168, 50, 157))
                        texto4 = fonte.render(texto_input[1],True,(168, 50, 157))
                        texto5 = fonte.render(texto_input[2],True,(168, 50, 157))
                        texto6 = fonte.render(texto_input[3],True,(168, 50, 157))
                        texto7 = fonte.render(texto_input[4],True,(168, 50, 157))
                        
                        if  texto_input[0] == palavra_chave[0]:
                            color = 'blue'
                        elif texto_input[0] in palavra_chave:
                            color = 'yellow'
                        else:
                            color = 'red'
                            
                        if  texto_input[1] == palavra_chave[1]:
                            color1 = 'blue'
                        elif texto_input[1] in palavra_chave:
                            color1 = 'yellow'
                        else:
                            color1 = 'red'
                            
                        if  texto_input[2] == palavra_chave[2]:
                            color2 = 'blue'
                        elif texto_input[2] in palavra_chave:
                            color2 = 'yellow'
                        else:
                            color2 = 'red'
                            
                        if  texto_input[3] == palavra_chave[3]:
                            color3 = 'blue'
                        elif texto_input[3] in palavra_chave:
                            color3 = 'yellow'
                        else:
                            color3 = 'red'
                            
                        if texto_input[4] == palavra_chave[4]:
                            color4 = 'blue'
                        elif texto_input[4] in palavra_chave:
                            color4 = 'yellow'
                        else:
                            color4 = 'red'
                        texto_input = ''
                        tentativa = 1
                        
                elif ev.type == KEYDOWN and tentativa == 1 and ev.key == K_RETURN: #checa se qualquer botao foi clicado
                        list(texto_input)
                        if texto_input == palavra_chave:
                            texto_final1 = fonte.render('VOCE ACERTOU A PALAVRA!!!!',True,('black'))
                        fonte = font.Font(None,40)
                        texto8 = fonte.render(texto_input[0],True,(168, 50, 157))
                        texto9 = fonte.render(texto_input[1],True,(168, 50, 157))
                        texto10 = fonte.render(texto_input[2],True,(168, 50, 157))
                        texto11 = fonte.render(texto_input[3],True,(168, 50, 157))
                        texto12 = fonte.render(texto_input[4],True,(168, 50, 157))
                        if  texto_input[0] == palavra_chave[0]:
                            color6 = 'blue'
                        elif texto_input[0] in palavra_chave:
                            color6 = 'yellow'
                        else:
                            color6 = 'red'
                            
                        if  texto_input[1] == palavra_chave[1]:
                            color7 = 'blue'
                        elif texto_input[1] in palavra_chave:
                            color7 = 'yellow'
                        else:
                            color7 = 'red'
                            
                        if  texto_input[2] == palavra_chave[2]:
                            color8 = 'blue'
                        elif texto_input[2] in palavra_chave:
                            color8 = 'yellow'
                        else:
                            color8 = 'red'
                            
                        if  texto_input[3] == palavra_chave[3]:
                            color9 = 'blue'
                        elif texto_input[3] in palavra_chave:
                            color9 = 'yellow'
                        else:
                            color9 = 'red'
                            
                        if texto_input[4] == palavra_chave[4]:
                            color10 = 'blue'
                        elif texto_input[4] in palavra_chave:
                            color10 = 'yellow'
                        else:
                            color10 = 'red'
                        texto_input = ''
                        tentativa = 2
                        
                elif ev.type == KEYDOWN and tentativa == 2 and ev.key == K_RETURN: #checa se qualquer botao foi clicado
                        list(texto_input)
                        if texto_input == palavra_chave:
                            texto_final1 = fonte.render('VOCE ACERTOU A PALAVRA!!!!',True,('black'))
                        fonte = font.Font(None,40)
                        texto13 = fonte.render(texto_input[0],True,(168, 50, 157))
                        texto14 = fonte.render(texto_input[1],True,(168, 50, 157))
                        texto15 = fonte.render(texto_input[2],True,(168, 50, 157))
                        texto16 = fonte.render(texto_input[3],True,(168, 50, 157))
                        texto17 = fonte.render(texto_input[4],True,(168, 50, 157))
                        if  texto_input[0] == palavra_chave[0]:
                            color11 = 'blue'
                        elif texto_input[0] in palavra_chave:
                            color11 = 'yellow'
                        else:
                            color11 = 'red'
                            
                        if  texto_input[1] == palavra_chave[1]:
                            color12 = 'blue'
                        elif texto_input[1] in palavra_chave:
                            color12 = 'yellow'
                        else:
                            color12 = 'red'
                            
                        if  texto_input[2] == palavra_chave[2]:
                            color13 = 'blue'
                        elif texto_input[2] in palavra_chave:
                            color13 = 'yellow'
                        else:
                            color13 = 'red'
                            
                        if  texto_input[3] == palavra_chave[3]:
                            color14 = 'blue'
                        elif texto_input[3] in palavra_chave:
                            color14 = 'yellow'
                        else:
                            color14 = 'red'
                            
                        if texto_input[4] == palavra_chave[4]:
                            color15 = 'blue'
                        elif texto_input[4] in palavra_chave:
                            color15 = 'yellow'
                        else:
                            color15 = 'red'
                        texto_input = ''
                        tentativa = 3

                elif ev.type == KEYDOWN and tentativa == 4 and ev.key == K_RETURN: #checa se qualquer botao foi clicado
                        list(texto_input)
                        if texto_input == palavra_chave:
                            texto_final1 = fonte.render('VOCE ACERTOU A PALAVRA!!!!',True,('black'))
                        fonte = font.Font(None,40)
                        textoa = fonte.render(texto_input[0],True,(168, 50, 157))
                        textob = fonte.render(texto_input[1],True,(168, 50, 157))
                        textoc = fonte.render(texto_input[2],True,(168, 50, 157))
                        textod = fonte.render(texto_input[3],True,(168, 50, 157))
                        textoe = fonte.render(texto_input[4],True,(168, 50, 157))
                        if  texto_input[0] == palavra_chave[0]:
                            color21 = 'blue'
                        elif texto_input[0] in palavra_chave:
                            color21 = 'yellow'
                        else:
                            color21 = 'red'
                            
                        if  texto_input[1] == palavra_chave[1]:
                            color22 = 'blue'
                        elif texto_input[1] in palavra_chave:
                            color22 = 'yellow'
                        else:
                            color22 = 'red'
                            
                        if  texto_input[2] == palavra_chave[2]:
                            color23 = 'blue'
                        elif texto_input[2] in palavra_chave:
                            color23 = 'yellow'
                        else:
                            color23 = 'red'
                            
                        if  texto_input[3] == palavra_chave[3]:
                            color24 = 'blue'
                        elif texto_input[3] in palavra_chave:
                            color24 = 'yellow'
                        else:
                            color24 = 'red'
                            
                        if texto_input[4] == palavra_chave[4]:
                            color25 = 'blue'
                        elif texto_input[4] in palavra_chave:
                            color25 = 'yellow'
                        else:
                            color25 = 'red'
                        texto_input = ''
                        tentativa = 5
                        
                elif ev.type == KEYDOWN and tentativa == 3 and ev.key == K_RETURN: #checa se qualquer botao foi clicado
                        list(texto_input)
                        if texto_input == palavra_chave:
                            texto_final1 = fonte.render('VOCE ACERTOU A PALAVRA!!!!',True,('black'))
                        fonte = font.Font(None,40)
                        texto18 = fonte.render(texto_input[0],True,(168, 50, 157))
                        texto19 = fonte.render(texto_input[1],True,(168, 50, 157))
                        texto20 = fonte.render(texto_input[2],True,(168, 50, 157))
                        texto21 = fonte.render(texto_input[3],True,(168, 50, 157))
                        texto22 = fonte.render(texto_input[4],True,(168, 50, 157))
                        if  texto_input[0] == palavra_chave[0]:
                            color16 = 'blue'
                        elif texto_input[0] in palavra_chave:
                            color16 = 'yellow'
                        else:
                            color16 = 'red'
                            
                        if  texto_input[1] == palavra_chave[1]:
                            color17 = 'blue'
                        elif texto_input[1] in palavra_chave:
                            color17 = 'yellow'
                        else:
                            color17 = 'red'
                            
                        if  texto_input[2] == palavra_chave[2]:
                            color18 = 'blue'
                        elif texto_input[2] in palavra_chave:
                            color18 = 'yellow'
                        else:
                            color18 = 'red'
                            
                        if  texto_input[3] == palavra_chave[3]:
                            color19 = 'blue'
                        elif texto_input[3] in palavra_chave:
                            color19 = 'yellow'
                        else:
                            color19 = 'red'
                            
                        if texto_input[4] == palavra_chave[4]:
                            color20 = 'blue'
                        elif texto_input[4] in palavra_chave:
                            color20 = 'yellow'
                        else:
                            color20 = 'red'
                        texto_input = ''
                        tentativa = 4
                        
                elif ev.type == KEYDOWN and ev.key == K_BACKSPACE:     
                    texto_input = texto_input[0:-1]
                else :
                    if ev.type == KEYDOWN:
                        texto_input += ev.unicode #qual botao especifico foi clicado e soma:
                    
                    
                if ev.type == QUIT:
                    quit()
                    sys.exit()
            texto1 = fonte.render(texto_input,True,(168, 50, 157))
            window.blit(texto1,(700,150))
            
    if estado_tela == JOGO3:
        if a == 1:
            desenhar_menu()
            estado_tela = MENU
            if 300 <= mouse_x <= 570 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO
            if 800 <= mouse_x <= 1070 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO2
            if 1290 <= mouse_x <= 1560 and 350 <= mouse_y <= 430:
                a = 0
                estado_tela = JOGO3
        
        clock.tick(60)
        window.fill('pink')
        
        # Desenha todos os botões da calculadora
        # Linha 1
        draw.rect(window, 'blue', (440, 250, 120, 80))
        texto_voumematar("C", 480, 270)

        draw.rect(window, 'blue', (580, 250, 120, 80))
        texto_voumematar("( )", 600, 270)

        draw.rect(window, 'blue', (720, 250, 120, 80))
        texto_voumematar("%", 760, 270)

        draw.rect(window, 'blue', (860, 250, 120, 80))
        texto_voumematar("÷", 900, 270)

        # Linha 2
        draw.rect(window, 'blue', (440, 350, 120, 80))
        texto_voumematar("7", 480, 370)

        draw.rect(window, 'blue', (580, 350, 120, 80))
        texto_voumematar("8", 620, 370)

        draw.rect(window, 'blue', (720, 350, 120, 80))
        texto_voumematar("9", 760, 370)

        draw.rect(window, 'blue', (860, 350, 120, 80))
        texto_voumematar("×", 900, 370)

        # Linha 3
        draw.rect(window, 'blue', (440, 450, 120, 80))
        texto_voumematar("4", 480, 470)

        draw.rect(window, 'blue', (580, 450, 120, 80))
        texto_voumematar("5", 620, 470)

        draw.rect(window, 'blue', (720, 450, 120, 80))
        texto_voumematar("6", 760, 470)

        draw.rect(window, 'blue', (860, 450, 120, 80))
        texto_voumematar("-", 900, 470)

        # Linha 4
        draw.rect(window, 'blue', (440, 550, 120, 80))
        texto_voumematar("1", 480, 570)

        draw.rect(window, 'blue', (580, 550, 120, 80))
        texto_voumematar("2", 620, 570)

        draw.rect(window, 'blue', (720, 550, 120, 80))
        texto_voumematar("3", 760, 570)

        draw.rect(window, 'blue', (860, 550, 120, 80))
        texto_voumematar("+", 900, 570)

        # Linha 5
        draw.rect(window, 'blue', (440, 650, 120, 80))
        texto_voumematar("+/-", 460, 670)

        draw.rect(window, 'blue', (580, 650, 120, 80))
        texto_voumematar("0", 620, 670)

        draw.rect(window, 'blue', (720, 650, 120, 80))
        texto_voumematar(".", 760, 670)

        draw.rect(window, 'blue', (860, 650, 120, 80))
        texto_voumematar("=", 900, 670)
        
        # Display da calculadora
        draw.rect(window, 'black', (440, 150, 540, 80))
        
        # Atualiza o texto do display
        text_result = fonte_global.render(textt, True, ('red'))
        window.blit(text_result, (450, 170))

        # Botão MENU
        draw.rect(window, 'white', (1000, 550, 200, 100))
        textov = fonte.render('MENU', True, (168, 50, 157))
        window.blit(textov, (1070, 580))

        for ev in event.get():
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                mouse_x, mouse_y = ev.pos
                
                # Verifica clique no MENU
                if (1000 <= mouse_x <= 1200) and (550 <= mouse_y <= 650):
                    a = 1
                    estado_tela = MENU
                
                # Botões da calculadora
                # Números
                elif (440 <= mouse_x <= 560) and (550 <= mouse_y <= 630):  # 1
                    textt += '1'
                elif (580 <= mouse_x <= 700) and (550 <= mouse_y <= 630):  # 2
                    textt += '2'
                elif (720 <= mouse_x <= 840) and (550 <= mouse_y <= 630):  # 3
                    textt += '3'
                elif (440 <= mouse_x <= 560) and (450 <= mouse_y <= 530):  # 4
                    textt += '4'
                elif (580 <= mouse_x <= 700) and (450 <= mouse_y <= 530):  # 5
                    textt += '5'
                elif (720 <= mouse_x <= 840) and (450 <= mouse_y <= 530):  # 6
                    textt += '6'
                elif (440 <= mouse_x <= 560) and (350 <= mouse_y <= 430):  # 7
                    textt += '7'
                elif (580 <= mouse_x <= 700) and (350 <= mouse_y <= 430):  # 8
                    textt += '8'
                elif (720 <= mouse_x <= 840) and (350 <= mouse_y <= 430):  # 9
                    textt += '9'
                elif (580 <= mouse_x <= 700) and (650 <= mouse_y <= 730):  # 0
                    textt += '0'
                
                # Operadores
                elif (860 <= mouse_x <= 980) and (550 <= mouse_y <= 630):  # +
                    textt += '+'
                elif (860 <= mouse_x <= 980) and (450 <= mouse_y <= 530):  # -
                    textt += '-'
                elif (860 <= mouse_x <= 980) and (350 <= mouse_y <= 430):  # ×
                    textt += '*'
                elif (860 <= mouse_x <= 980) and (250 <= mouse_y <= 330):  # ÷
                    textt += '/'
                elif (720 <= mouse_x <= 840) and (250 <= mouse_y <= 330):  # %
                    textt += '*0.01*'
                elif (720 <= mouse_x <= 840) and (650 <= mouse_y <= 730):  # .
                    textt += '.'
                
                # Funções especiais
                elif (440 <= mouse_x <= 560) and (250 <= mouse_y <= 330):  # C
                    textt = ''
                elif (580 <= mouse_x <= 700) and (250 <= mouse_y <= 330):  # ( )
                    if '(' in textt and textt.count('(') > textt.count(')'):
                        textt += ')'
                    else:
                        textt += '('
                elif (440 <= mouse_x <= 560) and (650 <= mouse_y <= 730):  # +/-
                    if textt and textt[0] == '-':
                        textt = textt[1:]
                    elif textt:
                        textt = '-' + textt
                
                # Botão de igual (=)
                elif (860 <= mouse_x <= 980) and (650 <= mouse_y <= 730):  # =
                    try:
                        # Substitui símbolos para avaliação segura
                        result = str(eval(textt))
                        textt = result
                    except:
                        textt = "Erro"

    display.update()