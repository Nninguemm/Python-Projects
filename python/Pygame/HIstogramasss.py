from pygame import *
from pygame.locals import QUIT
import sys
import random


def Color2():
    return random.randint(1,255), random.randint(1,255) , random.randint(1,255)


def histograma(nums,categ_nums):
    nums.sort() #coloca os numeros em ordem

    tamanho_categ = [len(nums)//categ_nums]* categ_nums #separa igualmente a quantidade de elementos em cada coluna

    for i in range(len(nums)%categ_nums): # caso não tenha tido uma divisao inteira, adiciona elementos sobrando a(s) primeira(s) coluna(s)
        tamanho_categ[i] += 1

    return tamanho_categ # retorna uma lista de cada elemento separado em sua respectiva coluna


def histograma_tristeza(nums,categ_nums):
    nums.sort() #coloca os numeros em ordem

    tamanho_categ = [1]*categ_nums
    x = len(nums) - categ_nums
    for i in range(categ_nums):
        if x > 0:
            b = random.randint(1,x)
            tamanho_categ[i] += b
            x -= b

    return tamanho_categ
    
        

nums1 = [100,200,300,400,500,600,700,800,900,1000,150,250,350,450,800,900,2,4] #lista dos elementos do histograma
nums2 = random.sample((range(1,2000)),67)
nums3 = []
categ_nums1 = 6  #quantidade de colunas
categ_nums2 = 10
categ_nums3 = 7

lista_tam_catego = histograma_tristeza(nums1,categ_nums1)
lista_tam_catego2 = histograma(nums2,categ_nums2)
lista_tam_catego3 = histograma(nums3,categ_nums3)

colores = [Color2(), Color2(), Color2(), Color2(), Color2(), Color2(), Color2(), Color2(), Color2(), Color2(), Color2()]

init()
tela = display.set_mode((1200,900))
textoi = ''
listi = []
H1 = 'histo1'
H2 = 'histo2'
H3 = 'histo3'
modo = H1
var1 = 0


#loop
while True:
    tela.fill((235, 255, 255))
    mouse_x, mouse_y = mouse.get_pos()
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
            
        if modo == H1:
            if ev.type == MOUSEBUTTONDOWN:
                if (900 <= mouse_x <= 1080) and (500 <= mouse_y <= 580):
                    modo = H2
        if modo == H2:
            if ev.type == MOUSEBUTTONDOWN:
                if (900 <= mouse_x <= 1080) and (300 <= mouse_y <= 380):
                    modo = H3
                if (20 <= mouse_x <= 200) and (300 <= mouse_y <= 380):
                    modo = H1
        if modo == H3:
            if ev.type == MOUSEBUTTONDOWN:
                if (30 <= mouse_x <= 210) and (500 <= mouse_y <= 580):
                    modo = H2
            if ev.type == KEYDOWN and ev.key == K_RETURN:
                textoc = int(textoi)
                listi.append(textoc)
                print(listi)
                textoi = ''
            elif ev.type == KEYDOWN and ev.key == K_BACKSPACE:     
                textoi = textoi[0:-1]
            elif ev.type == KEYDOWN and ev.key == K_f:
                nums3 = listi
                print(nums3)
            else :
                if ev.type == KEYDOWN:
                    textoi += ev.unicode 


    
    if modo == H1:   
        for i in range(len(lista_tam_catego)):
            max_altura = max(lista_tam_catego) if lista_tam_catego else 1

            altura = 600*lista_tam_catego[i]/max(lista_tam_catego) #pega a altura(y) de cada retangulo
            posx = 50*i + 400 #pega a posição de inicio de cada retangulo
            draw.rect(tela,(colores[i]),(posx,850 - altura,35,altura)) #desenha o os retangulos
            draw.line(tela,'black',(400,850),(800,850),5)
            draw.line(tela,'black',(395,850),(395,200),5)
            draw.rect(tela,'purple',(900,500,180,80))
            fontez = font.Font(None,40)
            text = fontez.render('Histograma 2',True,'red')
            tela.blit(text,(900,510))
            nums1.sort()
            fontez = font.Font(None,20)
            intervalo = (nums1[-1] - nums1[0]) / categ_nums1
            for i in range(categ_nums1):
                inicio = nums1[0] + i * intervalo
                texto = fontez.render(f"{inicio:.0f}", True, 'red')  
                tela.blit(texto, (400 + 50 * i, 860))
            for i in range(5):
                valor = int(max_altura * (5 - i) / 5)
                texto = fontez.render(str(valor), True, 'red')
                tela.blit(texto, (370, 200 + i * 150))
            
            
            
    if modo == H2:
        for i in range(len(lista_tam_catego2)):
            altura = 600*lista_tam_catego2[i]/max(lista_tam_catego2)
            posx = 50*i + 250
            draw.rect(tela,(colores[i]),(posx,850 - altura,35,altura))
            draw.line(tela,'black',(250,850),(900,850),5)
            draw.line(tela,'black',(250,850),(250,200),5)
            draw.rect(tela,'purple',(900,300,180,80))
            fontez = font.Font(None,40)
            text = fontez.render('Histograma 3',True,'red')
            tela.blit(text,(900,310))
            draw.rect(tela,'purple',(20,300,180,80))
            text = fontez.render('Histograma 1',True,'red')
            tela.blit(text,(20,310))
            nums2.sort()
            fontez = font.Font(None,20)
            text = fontez.render(str(nums2[i]),True,'red')
            tela.blit(text,(posx,855))
            for i in range(lista_tam_catego2[0] + 1):
                text2 = fontez.render(str(len(nums2[0:(67//10 + 1) - i])),True,'red')
                tela.blit(text2,(230,(600*(7+i)/7) - 350 ))
                      
    if modo == H3:
        for i in range(len(lista_tam_catego3)):
            fontez = font.Font(None,30)
            text = fontez.render('digite um elemento (ao clicar enter o elemento será adicionado a uma sequencia )',True,'red')
            tela.blit(text,(100,70))
            text = fontez.render('digite "F" quando terminar (é preciso no mínimo de 7 elementos)',True,'red')
            tela.blit(text,(100,100))
            textoy = str(textoi)
            text = fontez.render(textoy,True,'blue')
            tela.blit(text,(100,130))
            draw.rect(tela,'purple',(30,500,180,80))
            fontez = font.Font(None,40)
            text = fontez.render('Histograma 2',True,'red')
            tela.blit(text,(30,510))
            if nums3 == listi and nums3 != []:
                lista_tam_catego3 = histograma(nums3,categ_nums3)
                altura = 600*lista_tam_catego3[i]/max(lista_tam_catego3)
                posx = 50*i + 400
                draw.rect(tela,(colores[i]),(posx,850 - altura,35,altura))
                draw.line(tela,'black',(400,850),(1100,850),5)
                draw.line(tela,'black',(395,850),(395,200),5)
                nums2.sort()
                fontez = font.Font(None,20)
                text = fontez.render(str(nums3[i]),True,'red')
                tela.blit(text,(posx,855))
                for i in range(lista_tam_catego3[0] + 1):
                    text2 = fontez.render(str(len(nums3[0:(len(lista_tam_catego3)//10 + 1) - i])),True,'red')
                    tela.blit(text2,(370,(600*(7+i)/7) - 350 ))
                
    display.update()