from object import Ball
import pygame
import window_functions as wf
import time
class Score:

    def __init__(self,window:wf.Window,score_coordinate1,score_coordinate2,size,location1,location2) -> None:
        #REFERENCE WINDOW OBJECT
        self.window = window

        #Coordinates
        self.score_coordinate1 = score_coordinate1
        self.score_coordinate2 = score_coordinate2

        #PUT ALL IMAGES IN ARRAY
        self.score_img_array = []
        try:
            for i in range(7):
                self.score_img_array.append((pygame.transform.scale(pygame.image.load(location1.format(i)).convert_alpha(),size),
                pygame.transform.scale(pygame.image.load(location2.format(i)).convert_alpha(),size)))
        except Exception:
            pass

        #SCORE OF TWO TEAMS
        self.left_score = 0
        self.right_score = 0


        self.init()

    def init(self):
        self.window.screen.blit(self.score_img_array[self.left_score][0],self.score_coordinate1)
        self.window.screen.blit(self.score_img_array[self.right_score][1],self.score_coordinate2)

    #GOAL BOUNDARY
    def goal_win_checker(self,players,ball:Ball,score_bound_tuple):

        #FOR LEFT but score on right
        if ( (self.window.screen.get_height()*score_bound_tuple[0]/100) < ball.y < (self.window.screen.get_height()*score_bound_tuple[1]/100) and 
        (ball.x <= ball.radius)):
            self.right_score += 1
            self.goal_animation("Goal")
            ball.bring_in_center()
            for player in players:
                player.respawn()


        #FOR RIGHT but score on left
        if ( (self.window.screen.get_height()*score_bound_tuple[0]/100) < ball.y < (self.window.screen.get_height()*score_bound_tuple[1]/100) and 
        (ball.x + ball.radius >= self.window.screen.get_width())):
            self.left_score+= 1
            self.goal_animation("Goal")
            ball.bring_in_center()
            for player in players:
                player.respawn()

        #WHO WON AND THEN RESET SCORE
        if self.left_score == len(self.score_img_array) - 1:
            self.goal_animation("Blue Won")
            self.reset_score()
        elif self.right_score == len(self.score_img_array) - 1:
            self.goal_animation("Orange Won")
            self.reset_score()

    def goal_animation(self,texts):
        try:
            for font_size in range(2,64,2):
                #GOAL TEXT
                self.font = pygame.font.Font('font/arial.ttf', font_size)
                self.text = self.font.render(texts, True, (255, 255, 255))
                self.textRect = self.text.get_rect()
                self.textRect.center = (self.window.screen.get_width() // 2, self.window.screen.get_height() // 2)

                #update background (ALWAYS FIRST)
                self.window.blit_background()

                self.window.screen.blit(self.text, self.textRect)


                #update pygame display
                self.window.update()

            time.sleep(2)
            pass
        except Exception:
            pass

    def reset_score(self):
        self.left_score = 0
        self.right_score = 0
