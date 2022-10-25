import sys
import pygame
import time
from pygame import mixer
#import music

pygame.init()
mixer.init()
#music.init()

#from gamekeeper import Gamekeeper

# definer variabler
direction=1
width=900
height=500
speed=8
sigtekorn_ypos=160
sigtekorn_xpos=337
target_ypos=221
target_xpos=337
# farver
white=(250,250,250)
snehvid=(255,255,255)
sort=(0,0,0)
blå=(0,0,255)
# klapper
klap_x = 327
klap_y = 209
interval = 23

#set screen
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Winter Games 2022 - Amager Fælled")
#font for text
nyfont = pygame.font.SysFont("arial",25,bold=True)
# init clock from time
clock=pygame.time.Clock()

# load billeder til skærm
startbut=pygame.image.load("resources/start.jpeg")
baggrund=pygame.image.load("resources/wg_baggrund3.png")
sigtekorn=pygame.image.load("resources/crosshair3.png")
target=pygame.image.load("resources/crosshair3.png")
klap=pygame.image.load("resources/klap.png")

# load lydfiler
#intro=pygame.mixer.music.load('lotus_title.mp3')
gunshot = pygame.mixer.Sound("resources/gunshot.wav")
reload = pygame.mixer.Sound("resources/gun-cocking.wav")
title = pygame.mixer.Sound("resources/lotus_title.mp3")
#title = "C:\Users\runeh\PycharmProjects\wg3\resources"
#title = "C:\Users\runeh\Downloads\winter_games\gun-gunshot-02.wav"
#pygame.mixer.music.load(title)

# gamekeeper
active = False
counter = 0
gamedict={"counter":counter, "skud":8}

#start the loop
while True:
    # har jeg skud i bøssen?
    if gamedict["skud"]==0:
        #text_gameover = nyfont.render(f'Du har ikke flere patroner!', True, (blå), (snehvid))
        #screen.fill(white)
        #screen.blit(text_gameover, (230, 350))
        active = False
        time.sleep(3)
        pygame.quit()
        sys.exit()
    else:
        # check events with for-loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # hvad sker der?
                pygame.mixer.Sound.play(gunshot)
                gamedict["skud"] = gamedict["skud"] - 1
                time.sleep(0.8)
                pygame.mixer.Sound.play(reload)
                if sigtekorn_rect.colliderect(target_rect):
                    # tæl antal træf
                    gamedict["counter"] = gamedict["counter"] + 1
                    # intern review af tæller
                    print(f'score:{gamedict["counter"]}')
                    # flyt sigtekorn
                    sigtekorn_xpos=sigtekorn_xpos + interval
                    # flyt target
                    target_xpos=target_xpos + interval

                    # tegn cirkel for ramt target
                    #pygame.draw.circle(screen, (255, 255, 255), (target_xpos, target_ypos), 7)



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    #active=not active
                    active=True

                    # tilbage til start
                    #gamedict["counter"] = 0
                    #gamedict["skud"] = 8
                    #nulstil xpos
        #put background on screen
        screen.blit(baggrund,(0,0))
        if gamedict["counter"] > 0:
            screen.blit(klap,(klap_x, klap_y))
        if gamedict["counter"] > 1:
            screen.blit(klap, ((klap_x+interval), klap_y))
        if gamedict["counter"] > 2:
            screen.blit(klap, ((klap_x+interval*2), klap_y))
        if gamedict["counter"] > 3:
            screen.blit(klap, ((klap_x+interval*3), klap_y))
        if gamedict["counter"] > 4:
            screen.blit(klap, ((klap_x+interval*4), klap_y))
        if not active:
            #screen.fill(white)
            #screen.blit(startbut,(300,250))
            text_welcome=nyfont.render(f'Velkommen! Tryk S for at starte spillet',True,(blå),(snehvid))
            screen.blit(text_welcome, (230, 370))
            #pygame.mixer.music.play()
            #pygame.mixer.Sound.play(title)
        # spillets grafik
        else:
            # sigtet uroligt pga skyttens puls
            sigtekorn_ypos = sigtekorn_ypos + (speed * direction)
            if sigtekorn_ypos < 160 or sigtekorn_ypos > 320:
                direction = direction * -1
            sigtekorn_rect = sigtekorn.get_rect(center=(sigtekorn_xpos, sigtekorn_ypos))
            target_rect = target.get_rect(center=(target_xpos, target_ypos))
            #put counter on screen
            text_counter=nyfont.render(f'Træffere: {gamedict["counter"]}       Patroner: {gamedict["skud"]}',True,(sort),(snehvid))
            #put objects on screen
            screen.blit(text_counter,(250,370))
            if gamedict["counter"] < 5:
                screen.blit(sigtekorn,sigtekorn_rect)
            #if gamedict["counter"] == 5:
                #active = False
                # tillykkebillede
            #screen.blit(target,target_rect)
        #opdater skærm
        pygame.display.update()
        #tick the clock
        clock.tick(30)