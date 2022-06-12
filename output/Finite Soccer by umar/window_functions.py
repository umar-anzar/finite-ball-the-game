import pygame, sys

class Window():
    #Constructor
    def __init__(self,width=800,height=600,title="pygame",icon=None,color="#000000",bg_image=None):
        
        
        #set size, title, icon
        self.screen = pygame.display.set_mode((width,height))
        self.set_title(title)
        self.set_icon(icon)


        #set backgroundcolor, background image
        self.bg_color = self.set_background(color)
        self.bg_image = self.set_background_image(bg_image)
        self.blit_background()

        #window intialize
        pygame.init()


    def set_title(self,game_name):
        pygame.display.set_caption(game_name)

    def get_title(self):
        return pygame.display.get_caption()

    def set_icon(self,location):
        if location:
            pygame.display.set_icon( pygame.image.load(location) )
    
    def set_background(self,color):
        self.screen.fill(pygame.Color(color))
        return color

    def set_background_image(self,location):
        if location:
            bg_img = pygame.image.load(location).convert()
            bg_img.set_alpha(200)
            bg_img = pygame.transform.scale(bg_img,self.screen.get_size())
            return bg_img

    #BLIT BACKGROUND
    def blit_background(self):
        self.screen.fill(pygame.Color(self.bg_color))
        if self.bg_image:
            self.screen.blit(self.bg_image,(0,0))


    #QUIT WINDOW    
    def quit_window(self,event_type):
        if event_type == pygame.QUIT: sys.exit()

    def update(self):
        pygame.display.update()
    
