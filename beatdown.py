import pygame
import sys
import notes
import time
import music

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Notes
loaded_song = notes.load_song('example')
tempo = loaded_song['tempo']
start_time = time.time()

music.start_music()

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

index = 0
triangle_points = [(25,0),(25,50),(50,25)]
elapsed_time = 0


class NoteButton:
    def __init__(self, x,y, width, hight, player_number, button):
        self.player = player_number
        self.rect = pygame.Rect(x, y, width, hight)
        self.button = button
        self.surface = pygame.Surface((50,50))
        self.surface.set_colorkey((0,0,0)) 
        pygame.draw.polygon(self.surface,(255,0,0),triangle_points)

        if self.button == 1:
            self.surface = pygame.transform.rotate(self.surface, -180)
        elif self.button == 2:
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.button == 3:
            self.surface = pygame.transform.rotate(self.surface, 90)

    def draw(self):
        #pygame.draw.polygon(self.surface,(255,0,0),triangle_points)
        screen.blit(self.surface, self.rect)
        self.rect.y -= 2

# 0 = right, 1 = down, 2 = left, 3 = up
player_1_left = NoteButton(100,550,50,50,1,1)
player_1_down = NoteButton(160,550,50,50,1,2)
player_1_up = NoteButton(210,550,50,50,1,3)
player_1_right = NoteButton(260,550,50,50,1,0)

player_2_left = NoteButton(450,550,50,50,2,1)
player_2_down = NoteButton(510,550,50,50,2,2)
player_2_up = NoteButton(560,550,50,50,2,3)
player_2_right = NoteButton(610,550,50,50,2,0)

player_1_list = []
player_2_list = []

song_length = len(loaded_song["tracks"][0])

def Button_check(beat,song_length,loaded_song):
    #print(notes.get_buttons(beat,loaded_song))
    beat_list = notes.get_buttons(beat,loaded_song)

    if beat_list[0] == 1:
            
        player_1_list.append(NoteButton(260,550,50,50,1,0))
        player_2_list.append(NoteButton(610,550,50,50,2,0))
        
    if beat_list[1] == 1:
        
        player_1_list.append(NoteButton(160,550,50,50,1,2))
        player_2_list.append(NoteButton(510,550,50,50,2,2))

    if beat_list[2] == 1:
        player_1_list.append(NoteButton(100,550,50,50,1,1))
        player_2_list.append(NoteButton(450,550,50,50,2,1))

    if beat_list[3] == 1:
            
        player_1_list.append(NoteButton(210,550,50,50,1,3))
        player_2_list.append(NoteButton(560,550,50,50,2,3))
        
    #print(beat)


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
    
    dt = clock.tick(FPS)
    #print("dt: ", dt)
    elapsed_time += dt
    #print("elapsed ", elapsed_time)

    if elapsed_time / 1000 >= tempo / 60: #time between beats
        Button_check(index,song_length,loaded_song)
        elapsed_time = 0
        
        index += 1
        
    
    current_time = time.time() - start_time
    #current_beat = notes.get_beat(current_time, tempo)
    #buttons = notes.get_buttons(current_beat, loaded_song)
    #print('left needs to be pressed:', buttons[0])

    if player_1_list:
        for note in player_1_list:
            note.draw()

    if player_2_list:
        for note in player_2_list:
            note.draw()

    pygame.display.flip()


pygame.quit()
sys.exit()
