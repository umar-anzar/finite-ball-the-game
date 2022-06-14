def main():
    import pygame
    import window_functions as wf
    import objects
    import score

    #Window Specification---------------------------------------------------------------------------------------------------
    SCREEN_WIDTH = 1000 # width (in px)
    SCREEN_HEIGHT = 600 # height (in px)
    COLOR = "#FE9A00"
    ICON = "images/window_icon/icons8_football_kick_256.png"
    BG_IMAGE = "images/background/soccer-field.jpg"


    #INTIALIZE WINDOW OBJECT
    window = wf.Window(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="FINITE_BALL by Umar Anzar",icon=ICON,bg_image=BG_IMAGE)


    #SCORE------------------------------------------------------------------------------------------------------------------
    SIZE = (100,100)
    score_coordinate1 = (0,0)
    score_coordinate2 = (SCREEN_WIDTH-100,0)
    SCORE_LOCATION1 = 'images/score/score1/score_{}.png'
    SCORE_LOCATION2 = 'images/score/score2/score_{}.png'
    score_obj = score.Score(window,score_coordinate1,score_coordinate2,SIZE,SCORE_LOCATION1,SCORE_LOCATION2)
    SCORE_BOUNDARY_PERCENT = (41.66,57.5)

    #Player-----------------------------------------------------------------------------------------------------------------
    x1, x2 = SCREEN_WIDTH * 20/100, SCREEN_WIDTH * 80/100
    y1, y2 = SCREEN_HEIGHT // 2, SCREEN_HEIGHT// 2
    try:
        with open("speed.txt",'r') as file:
                FPS = int(eval(file.read()))
    except Exception:
        FPS = 5
    print("Speed set to: ",FPS)
    RADIUS = 15
    USER_COLOR1 = "#1CB3FF"
    USER_COLOR2 = "#FFA500"

    KEYBTN2 = {     pygame.K_RIGHT:0,   # right
                    pygame.K_LEFT:1,    # left
                    pygame.K_UP:2,      # up
                    pygame.K_DOWN:3,    # down
                    pygame.K_k:4}       # sprint
                    
    KEYBTN1 = {     pygame.K_d:0,
                    pygame.K_a:1,
                    pygame.K_w:2,
                    pygame.K_s:3,
                    pygame.K_SPACE:4}

    KEYBTN3 = {     pygame.K_KP_6:0,
                    pygame.K_KP_4:1,
                    pygame.K_KP_8:2,
                    pygame.K_KP_5:3,
                    pygame.K_KP_0:4}


    user1 = objects.Player(window,x1,y1,FPS,RADIUS,USER_COLOR1,KEYBTN1)
    user2 = objects.Player(window,x2,y2,FPS,RADIUS,USER_COLOR2,KEYBTN2)

    #BALL-------------------------------------------------------------------------------------------------------------------
    x =  SCREEN_WIDTH//2
    y =  SCREEN_HEIGHT//2
    FPS = 0
    BALL_RADIUS = 15
    BALL_COLOR = "#FF2222"


    ball = objects.Ball(window,x,y,FPS,BALL_RADIUS,BALL_COLOR)


    #BOUNDARY---------------------------------------------------------------------------------------------------------------
    X_LOWER_BOUND, X_UPPER_BOUND = RADIUS, SCREEN_WIDTH - RADIUS
    Y_LOWER_BOUND, Y_UPPER_BOUND = RADIUS, SCREEN_HEIGHT - RADIUS

    X_BALL_LOWER_BOUND, X_BALL_UPPER_BOUND = BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS
    Y_BALL_LOWER_BOUND, Y_BALL_UPPER_BOUND = BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS

    #GAME FPS---------------------------------------------------------------------------------------------------------------
    try:
        with open("fps.txt",'r') as file:
                GAME_FPS = int(eval(file.read()))
    except Exception:
        GAME_FPS = 60

    print("Game fps set to: ",GAME_FPS)
    clock = pygame.time.Clock()

    #PROGRAM LOOP-----------------------------------------------------------------------------------------------------------
    while True:

        #FPS OF GAME
        clock.tick(GAME_FPS)


        #update backgrund (ALWAYS FIRST)
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

        #GOAL OR MATCH WIN FUNCTION
        score_obj.goal_win_checker((user1,user2),ball,SCORE_BOUNDARY_PERCENT)

        # ACTION OF USER IN LOOP
            # MOVE THE USER
        user1.move()
        user2.move()
        ball.move()



        #need updating the user, ball, score
        user1.init()
        user2.init()
        ball.init()
        score_obj.init()


        #update pygame display
        window.update()
