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
FPS = 0.4
RADIUS = 15
USER_COLOR = "#1E53C6"
KEYBTN1 = {     pygame.K_RIGHT:0,
                pygame.K_LEFT:1,
                pygame.K_UP:2,
                pygame.K_DOWN:3,
                pygame.K_SPACE:4}
                
KEYBTN2 = {     pygame.K_d:0,
                pygame.K_a:1,
                pygame.K_w:2,
                pygame.K_s:3,
                pygame.K_SPACE:4}


user1 = player.Player(window,x,y,FPS,RADIUS,USER_COLOR,KEYBTN1)
user2 = player.Player(window,x,y,FPS,RADIUS,USER_COLOR,KEYBTN2)


#BOUNDARY
X_LOWER_BOUND, X_UPPER_BOUND = RADIUS, SCREEN_WIDTH - RADIUS
Y_LOWER_BOUND, Y_UPPER_BOUND = RADIUS, SCREEN_HEIGHT - RADIUS

while True:
    
    #ITERATION ON ALL THE EVENT TYPE
    for event in pygame.event.get():

        # TO EXIT/QUIT the game
        window.quit_window(event.type)

        # IF EVENT is key pressed so user perform action
        user1.transition(event)
        user2.transition(event)



    #CHECK BOUNDARY AND STOP MOVEMENT IF COLLIDE
    user1.user_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)
    user2.user_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)


    # ACTION OF USER IN LOOP
        # MOVE THE USER
    user1.move()
    user2.move()

    #update background
    window.blit_background()

    #need updating the user
    user1.init()
    user2.init()



    #update pygame display
    window.update()