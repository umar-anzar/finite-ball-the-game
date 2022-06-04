from curses import KEY_RIGHT
import imp
from shutil import move
from turtle import width
import pygame
import window_functions as wf
import player

#Window Specification
SCREEN_WIDTH = 900 # width (in px)
SCREEN_HEIGHT = 600 # height (in px)
COLOR = "#FE9A00"
ICON = "../images/hitman_480px.png"
BG_IMAGE = "../images/background_image.jpg"

#INTIALIZE WINDOW OBJECT
window = wf.Window(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Hitman",icon=ICON,color=COLOR,bg_image=BG_IMAGE)

#player
x=100
y=100
FPS = 0.1
RADIUS = 15
USER_COLOR = "#1E53C6"
user = player.User(window,x,y,FPS,RADIUS,USER_COLOR)


while True:
    
    #ITERATION ON ALL THE EVENT TYPE
    for event in pygame.event.get():

        # TO EXIT/QUIT the game
        window.quit_window(event.type)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                user.fps = 0.1

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_RIGHT:
                user.fps = 0
    user.move()
    #update background
    window.blit_background()

    #need updating the user
    user.init()


    

    #update pygame display
    window.update()