import pygame
import time 
import random

"""
Welcome to King in the North Car racing game, in this game the user 
is expected to dodge the upcoming cars. The user should use the left key
to move the car into left side and the right key to shift to the right.

The user can play endless time for now, i haven't implimented the lives 
count down function yet

NB: Dont mind the black car standing on the field, i used a pre-defined
background image.

"""

pygame.init() 
gray=(60,60,60)
black=(255,0,0) 
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("King In The North Car Game")    
my_car = pygame.image.load('car12.png')
my_strips = pygame.image.load('strips1.png')
backgroundleft=pygame.image.load("plain.jpeg")
# backgroundright=pygame.image.load("grass.png")
backgroundstrips=pygame.image.load("strips1.png")
car_width=23

def car(x,y): 
    screen.blit(my_car,(x,y))

def background():
    """
    This function creates the background of the game
    but due to struggle to find small width images i used 
    an pre_defined image for my background

    """
    # screen.blit(backgroundstrips,(400,200))
    # screen.blit(backgroundstrips,(400,400))
    
    screen.blit(backgroundleft,(0,0))
    # screen.blit(backgroundright,(700,0)) 


def obstacle_cars(obst_startx,obst_starty,obstacle):
    """
    This function creates the upcoming cars which are the obstacles
    that the user should dodge.

    It was suppose to print different cars coming at random, due to lake of images
    without a white background, only one type was used.

    """
    if obstacle==0:
        obstacle=pygame.image.load("car3.png") 
    if obstacle==1:
        obstacle=pygame.image.load("car3.png")
    if obstacle==2:
        obstacle=pygame.image.load("car3.png") 
    
    screen.blit(obstacle,(obst_startx,obst_starty))


def crash():       
    message_display("Car Crashed")

def message_display(text):     
    large_text=pygame.font.Font("freesansbold.ttf",80) 
    textsurf,textrect=text_object(text,large_text) 
    textrect.center=((500),(300)) 
    screen.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)     
    run_game()     

def text_object(text,font):    
    text_surface=font.render(text,True,black) 
    return text_surface,text_surface.get_rect()      


def run_game():  
    x=500 
    y=400 
    
    x_change=0 
    y_change=0
    
    obstacle_speed=15
    
    obstacle=0   
    obstacle_startx=random.randrange(130,(700-car_width))
    obstacle_starty=-600
    
    obstacle_width=23
    obstacle_height=47

    bumped=False

    while not bumped: 
    
        for event in pygame.event.get():   
            if event.type==pygame.QUIT:   
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN: 
                
                if event.key==pygame.K_LEFT: 
                    x_change=-5   
                if event.key==pygame.K_RIGHT: 
                    x_change=5     
            
            if event.type==pygame.KEYUP:   
                x_change=0
        x+=x_change
        screen.fill(gray) 
        background()
        obstacle_starty-=(obstacle_speed/1.2)   
        obstacle_cars(obstacle_startx,obstacle_starty,obstacle) 
        obstacle_starty+=obstacle_speed         
        car(x,y)   
        if x<130 or x>700-car_width:       
            crash()

                
        if obstacle_starty>600:     
            obstacle_starty=0-obstacle_height 
            obstacle_startx=random.randrange(130,(1000-300)) 
            obstacle=random.randrange(0,2)   

        if y<obstacle_starty+obstacle_height:
            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + car_width > obstacle_startx and x + car_width < obstacle_startx + obstacle_width :
                crash()       
                
        pygame.display.update() 
run_game() 
pygame.quit() 
quit()        