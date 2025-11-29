from pygame import *
import sys
from pygame.locals import QUIT

#time
clock = time.Clock()

#correr
perso = image.load('Run.png')
frame = 0
time_frame = 0
perso_invert = transform.flip(perso,True,False)
run = True

#personagem geral
pos_x = 0
estado_pers = perso
pos_y = 500

#atacar
attack = image.load('Attack_3.png')
time_frame_attack = 0
frame_attack = 0
attaca_inv = transform.flip(attack,True,False)
attacks = False

#pulo
jumps = image.load('Jump.png')
jump_inv = transform.flip(jumps,True,False)
time_jump = 0
frame_jump = 0
jump = False



#animacao constante samurai
perso2 = image.load('Run2.png')
nuvem = image.load('n.webp')
frame2 = 0
time_frame2 = 0
pos_x2 = 0

#tela
screen = display.set_mode((1200,800))

#loop do jogo
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
            
        #volta ao sprite original ao soltar o botão
        if ev.type == KEYUP:
            if ev.key == K_d:
                frame = 0
                time_fram = 0
            if ev.key == K_a:
                frame = 0
                time_fram = 0
                
        #botoes de ataque e pulo      
        if ev.type == KEYDOWN:
            if ev.key == K_e:
                attacks = True
            if ev.key == K_SPACE:
                jump = True

      
                
                
                
    #pega as teclas do teclado            
    keys = key.get_pressed()

    #tempoe fps
    clock.tick(60)
    dt = clock.get_time()
    
    #desenha as coisas
    screen.fill((124, 84, 19))
    draw.rect(screen,'green',(0,630,1200,25))
    nuvem = transform.scale(nuvem,(1550,200))
    screen.blit(nuvem, (-150,240))
    
    #correr,atacar e pular
    if run == True: 
        screen.blit(perso, (pos_x,500), (128*(frame%8),128*(frame//8),128,128))
    screen.blit(perso2, (pos_x2,200), (128*(frame2%8),128*(frame2//8),128,128))
    if attacks == True:
        screen.blit(estado_pers, (pos_x,500), (128*(frame_attack%4),128*(frame_attack//4),128,128))
    if jump == True:
        screen.blit(estado_pers, (pos_x,pos_y), (128*(frame_jump%12),128*(frame_jump//12),128,128))
        
    
    #andar direita
    if keys[K_d]:
        perso = image.load('Run.png')
        pos_x = pos_x + 0.3*dt
        time_frame += dt
        if time_frame > 150:
            frame += 1
            time_frame = 0
        if frame >= 8:
            frame = 0
            
    #andar esquerda           
    if keys[K_a]:
        perso = perso_invert
        pos_x = pos_x - 0.3*dt
        time_frame += dt
        if time_frame > 150:
            frame += 1
            time_frame = 0
        if frame >= 8:
            frame = 0
        if attacks == True:
            attack = attaca_inv
        if jump == True:
            jumps = jump_inv

            
            
    #personagem constante       
    pos_x2 = pos_x2 + 0.2*dt
    time_frame2 += dt
    if time_frame2 > 150:
        frame2 += 1
        time_frame2 = 0
    if frame2 >= 8:
        frame2 = 0      
    if pos_x2 > 1200:
        pos_x2 = -20
        
    #ataque
    if attacks == True:
        if jump == False:
            jump = False
            run = False
            estado_pers = attack
            if not keys[K_a]:
                attack = image.load('Attack_3.png')
            time_frame_attack += dt/1.5
            if time_frame_attack > 150:
                frame_attack += 1
                time_frame_attack = 0
            if frame_attack >= 4:
                frame_attack = 0
                estado_pers = perso
                run = True
                attacks = False
                jump = False
            
    #pulo
    if jump == True:
        run = False
        attacks = False
        estado_pers = jumps
        if not keys[K_a]:
            jumps = image.load('jump.png')
        pos_y = pos_y - 0.1*dt/4
        time_frame += dt
        time_jump += dt/1.5*2
        if time_jump > 150:
            frame_jump += 1
            time_jump = 0
        if frame_jump >= 6:
            pos_y = pos_y + 0.2*dt/4
        if frame_jump >= 12:
            frame_jump= 0
            estado_pers = jumps
            run = True
            jump = False
            attacks = False
    
    display.update()
    
    
    
    

