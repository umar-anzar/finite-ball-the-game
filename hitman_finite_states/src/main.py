import pygame
import window_functions as wf
import object

#Window Specification---------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 1000 # width (in px)
SCREEN_HEIGHT = 600 # height (in px)
COLOR = "#FE9A00"
ICON = "images/hitman_480px.png"
BG_IMAGE = "images/soccer-field.jpg"


#INTIALIZE WINDOW OBJECT
window = wf.Window(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="FINITE_BALL",icon=ICON,bg_image=BG_IMAGE)

#Player-----------------------------------------------------------------------------------------------------------------
x1, x2 = SCREEN_WIDTH * 20/100, SCREEN_WIDTH * 80/100
y1, y2 = SCREEN_HEIGHT // 2, SCREEN_HEIGHT// 2
FPS = 5
RADIUS = 15
USER_COLOR1 = "#1E53C6"
USER_COLOR2 = "#FFA500"

KEYBTN1 = {     pygame.K_RIGHT:0,   # right
                pygame.K_LEFT:1,    # left
                pygame.K_UP:2,      # up
                pygame.K_DOWN:3,    # down
                pygame.K_k:4}       # sprint
                
KEYBTN2 = {     pygame.K_d:0,
                pygame.K_a:1,
                pygame.K_w:2,
                pygame.K_s:3,
                pygame.K_SPACE:4}

KEYBTN3 = {     pygame.K_KP_6:0,
                pygame.K_KP_4:1,
                pygame.K_KP_8:2,
                pygame.K_KP_5:3,
                pygame.K_KP_0:4}


user1 = object.Player(window,x1,y1,FPS,RADIUS,USER_COLOR1,KEYBTN1)
user2 = object.Player(window,x2,y2,FPS,RADIUS,USER_COLOR2,KEYBTN2)

#BALL-------------------------------------------------------------------------------------------------------------------
x =  SCREEN_WIDTH//2
y =  SCREEN_HEIGHT//2
FPS = 0
BALL_RADIUS = 12
BALL_COLOR = "#FF2222"


ball = object.Ball(window,x,y,FPS,RADIUS,BALL_COLOR)


#BOUNDARY---------------------------------------------------------------------------------------------------------------
X_LOWER_BOUND, X_UPPER_BOUND = RADIUS, SCREEN_WIDTH - RADIUS
Y_LOWER_BOUND, Y_UPPER_BOUND = RADIUS, SCREEN_HEIGHT - RADIUS

X_BALL_LOWER_BOUND, X_BALL_UPPER_BOUND = BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS
Y_BALL_LOWER_BOUND, Y_BALL_UPPER_BOUND = BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS

#GAME FPS
GAME_FPS = 60
clock = pygame.time.Clock()

#PROGRAM LOOP-----------------------------------------------------------------------------------------------------------
while True:

    #FPS OF GAME
    clock.tick(GAME_FPS)


    #update background (ALWAYS FIRST)
    window.blit_background()


    #ITERATION ON ALL THE EVENT TYPE
    for event in pygame.event.get():

        # TO EXIT/QUIT the game
        window.quit_window(event.type)

        # IF EVENT is key pressed so user perform action
        user1.transition(event)
        user2.transition(event)


    #PLAYER HITS BALL
    ball.on_hit(user1)
    ball.on_hit(user2)

    #CHECK BOUNDARY AND STOP MOVEMENT IF COLLIDE
    user1.user_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)
    user2.user_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)
    ball.ball_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)
    ball.out_of_boundary(X_LOWER_BOUND, X_UPPER_BOUND, Y_LOWER_BOUND, Y_UPPER_BOUND)


    # ACTION OF USER IN LOOP
        # MOVE THE USER
    user1.move()
    user2.move()
    ball.move()



    #need updating the user and ball
    user1.init()
    user2.init()
    ball.init()



    #update pygame display
    window.update()
