import pygame
import sys
import notes
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Notes
loaded_song = notes.load_song('example')
tempo = loaded_song['tempo']
start_time = time.time()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BEATDOWN")
clock = pygame.time.Clock()

class Platform:
    def __init__(self,x,y,width,hight,color = (50,50,50)):
        self.rect = pygame.Rect(x,y,width,hight)
        self.color = color

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)

stage = Platform(100,250,600,350,(150,230,100))

class NoteButton:
    def __init__(self, position, type, player_number):
        self.position = position
        self.type = type
        self.player = player_number

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), self.position, 15)

# 0 = left, 1 = right, 2 = up, 3 = down
player_1_left = NoteButton((150, 300), 0, 0)

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

    current_time = time.time() - start_time
    current_beat = notes.get_beat(current_time, tempo)
    buttons = notes.get_buttons(current_beat, loaded_song)
    print('left needs to be pressed:', buttons[0])
    player_1_left.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
