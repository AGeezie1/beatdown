import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BEATDOWN")

clock = pygame.time.Clock()

keys = pygame.key.get_pressed()



class Platform:
    def __init__(self,x,y,width,hight,color = (50,50,50)):
        self.rect = pygame.Rect(x,y,width,hight)
        self.color = color

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)

#class Notes:
   # def __init__(self,x,y,width,hight,tempo,speed):


stage = Platform(100,250,600,350,(150,230,100))

    
running = True
while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_a:
                print("1 LEFT")
            if event.key == pygame.K_w:
                print("1 UP")
            if event.key == pygame.K_d:
                print("1 RIGHT")
            if event.key == pygame.K_s:
                print("1 DOWN")
            

            if event.key == pygame.K_LEFT:
                print("2 LEFT")
            if event.key == pygame.K_UP:
                print("2 UP")
            if event.key == pygame.K_RIGHT:
                print("2 RIGHT")
            if event.key == pygame.K_DOWN:
                print("2 DOWN")







            

    

    screen.fill((53,102,55))
    stage.draw(screen) 


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
