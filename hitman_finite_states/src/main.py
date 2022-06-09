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

#Player
x=100
y=100
FPS = 0.6
RADIUS = 15
USER_COLOR = "#1E53C6"
user = player.User(window,x,y,FPS,RADIUS,USER_COLOR)


#BOUNDARY
X_LOWER_BOUND, X_UPPER_BOUND = RADIUS, SCREEN_WIDTH - RADIUS
Y_LOWER_BOUND, Y_UPPER_BOUND = RADIUS, SCREEN_HEIGHT - RADIUS

while True:
    
    #ITERATION ON ALL THE EVENT TYPE
    for event in pygame.event.get():

        # TO EXIT/QUIT the game
        window.quit_window(event.type)

        # IF EVENT is key pressed so user perform action
        user.transition(event)



    #CHECK BOUNDARY AND STOP MOVEMENT IF COLLIDE
    if user.x < X_LOWER_BOUND or user.x > X_UPPER_BOUND:
        user.horizontal_factor = 0
    if user.y < Y_LOWER_BOUND or user.y > Y_UPPER_BOUND:
        user.vertical_factor = 0

    # ACTION OF USER IN LOOP
        # MOVE THE USER
    user.move()

    #update background
    window.blit_background()

    #need updating the user
    user.init()


    

    #update pygame display
    window.update()