from pygame import *
import pygame
class User:

    def __init__(self,window,x,y,fps,radius,color) -> None:
        #REFERENCE WINDOW OBJECT
        self.window = window

        #COORDINATES,RADIUS,COLOR,FRAME PER SECOND
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.fps = fps

        # DIRECTION FACTORS
        self.horizontal_factor = 0
        self.vertical_factor = 0

        # DOMAIN OF KEYS ACCEPTED
        self.domain = [K_RIGHT,K_LEFT,K_UP,K_DOWN,K_SPACE]

        self.pressed = set([])


        # INITIAL AND CURRENT STATE
        self.current = 0

        # FUNCTIONS OF EACH STATE
        self.statesFunction = [self.S0,self.S1,self.S2,self.S3,self.S4,self.S5]

        self.TransitionTable = [
            [(K_RIGHT,1),   (K_LEFT,2), (K_UP,3),   (K_DOWN,4), (K_SPACE,5)],
            [(K_RIGHT,1),   (K_UP,3),   (K_DOWN,4), (K_SPACE,5)],
            [(K_LEFT,2),    (K_UP,3),   (K_DOWN,4), (K_SPACE,5)],
            [(K_UP,3),      (K_LEFT,2), (K_RIGHT,1),(K_SPACE,5)],
            [(K_DOWN,4),    (K_LEFT,2), (K_RIGHT,1),(K_SPACE,5)],
            [(K_SPACE,5)]
        ]
        '''
        self.TransitionsTable = [
            [[(K_RIGHT,0),(K_LEFT,0),(K_UP,0),(K_DOWN,0),(K_SPACE,0)],  [(K_RIGHT,1),   (K_LEFT,2), (K_UP,3),   (K_DOWN,4), (K_SPACE,5)]],
            [[(K_RIGHT,0),(K_UP,0),(K_DOWN,0)],                         [(K_RIGHT,1),   (K_UP,3),   (K_DOWN,4), (K_SPACE,5)]],
            [[(K_LEFT,0),(K_UP,0),(K_DOWN,0)],                          [(K_LEFT,2),    (K_UP,3),   (K_DOWN,4), (K_SPACE,5)]],
            [[(K_UP,0),(K_RIGHT,0),(K_LEFT,0)],                         [(K_UP,3),      (K_LEFT,2), (K_RIGHT,1),(K_SPACE,5)]],
            [[(K_DOWN,0),(K_RIGHT,0),(K_LEFT,0)],                       [(K_DOWN,4),    (K_LEFT,2), (K_RIGHT,1),(K_SPACE,5)]],
            [[],[]]
        ]
        '''
        


        self.init()

    def init(self):
        pygame.draw.circle(self.window.screen,pygame.Color(self.color),(self.x,self.y),self.radius)


    def transition(self,keytype,key):

        if keytype == KEYUP:
            if key in self.domain:
                try:
                    self.pressed.remove(key)
                    self.current = 0
                    self.statesFunction[self.current]()
                    for action in self.pressed:
                        for connection in self.TransitionTable[self.current]:
                            if action == connection[0]:
                                self.current = connection[1]
                                self.statesFunction[self.current]()
                except:
                    pass
        else:

            for connection in self.TransitionTable[self.current]:
                if key == connection[0]:
                    self.current = connection[1]
                    self.pressed.add(key)
                    break
        
        self.statesFunction[self.current]()


        


    def move(self):
        if abs(self.horizontal_factor) == 1 and abs(self.vertical_factor) == 1:
            fps = ( (self.fps**2) /2)**(1/2)
        else:
            fps = self.fps

        self.x += self.horizontal_factor * fps
        self.y += self.vertical_factor * fps

    def S0(self):
        self.horizontal_factor,self.vertical_factor = 0,0
        self.move()

    def S1(self):
        self.horizontal_factor = 1
        self.move()    

    def S2(self):
        self.horizontal_factor= -1
        self.move()

    def S3(self):
        self.vertical_factor = -1
        self.move()

    def S4(self):
        self.vertical_factor = 1
        self.move()

    def S5(self):
        self.horizontal_factor,self.vertical_factor = 0,0
        self.move()
