import pygame
import window_functions as wf
class Score:

    def __init__(self,window:wf.Window,x,y,size,location) -> None:
        #REFERENCE WINDOW OBJECT
        self.window = window
        self.x,self.y = x,y
        self.score_img_array = []

        try:
            for i in range(10):
                self.score_img_array.append(pygame.transform.scale(pygame.image.load(location.format(i+1)).convert_alpha(),size))
        except Exception:
            pass
        self.current_score = 0


        self.init()

    def init(self):
        self.window.screen.blit(self.score_img_array[self.current_score],(self.x,self.y))