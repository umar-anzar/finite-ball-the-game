import pygame
class User:

    def __init__(self,window,x,y,fps,radius,color) -> None:
        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.fps = fps

        
        self.init()

    def init(self):
        pygame.draw.circle(self.window.screen,pygame.Color(self.color),(self.x,self.y),self.radius)

    def move(self):
        self.x += self.fps
