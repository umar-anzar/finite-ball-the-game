import pygame
import window_functions as wf
class Score:

    def __init__(self,window:wf.Window,x,y,size,location1,location2) -> None:
        #REFERENCE WINDOW OBJECT
        self.window = window
        self.x,self.y = x,y
        self.score_img_array = []

        try:
            for i in range(10):
                self.score_img_array.append((pygame.transform.scale(pygame.image.load(location1.format(i+1)).convert_alpha(),size),
                pygame.transform.scale(pygame.image.load(location2.format(i+1)).convert_alpha(),size)))
        except Exception:
            pass
        self.left_score = 0
        self.right_score = 0


        self.init()

    def init(self):
        x = self.window.screen.get_width() - self.score_img_array[self.left_score][1].get_width()
        self.window.screen.blit(self.score_img_array[self.left_score][0],(self.x,self.y))
        self.window.screen.blit(self.score_img_array[self.left_score][1],(x,self.y))