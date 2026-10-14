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

class TargetNote:
    def __init__(self,x,y,width,hight,player_number,button):
        self.player = player_number
        self.rect = pygame.Rect(x,y,width,hight)
        self.button = button
        self.surface = pygame.Surface((50,50))
        self.surface.set_colorkey((0,0,0)) 
        pygame.draw.polygon(self.surface,(0,200,0,0),triangle_points)

        if self.button == 1:
            self.surface = pygame.transform.rotate(self.surface, -180)
        elif self.button == 2:
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.button == 3:
            self.surface = pygame.transform.rotate(self.surface, 90)

    def draw(self):
        screen.blit(self.surface, self.rect)
        
class NoteButton:
    def __init__(self, x,y, width, hight, player_number, button):
        self.player = player_number
        self.rect = pygame.Rect(x, y, width, hight)
        self.button = button
        self.surface = pygame.Surface((50,50))
        self.surface.set_colorkey((0,0,0))
        self.visible = True
        pygame.draw.polygon(self.surface,(255,0,0,0),triangle_points)

        if self.button == 1:
            self.surface = pygame.transform.rotate(self.surface, -180)
        elif self.button == 2:
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.button == 3:
            self.surface = pygame.transform.rotate(self.surface, 90)

    def hide(self):
        if self.visible == True:
            self.visible = False
        
        

    def draw(self):
        #pygame.draw.polygon(self.surface,(255,0,0),triangle_points)
        if self.visible == True:
            screen.blit(self.surface, self.rect)
            self.rect.y -= 2

    

# 0 = right, 2 = down, 1 = left, 3 = up
'''
INFO FOR STARTING POSITIONS 
player_1_left = NoteButton(100,550,50,50,1,2)
player_1_down = NoteButton(160,550,50,50,1,1)
player_1_up = NoteButton(210,550,50,50,1,3)
player_1_right = NoteButton(260,550,50,50,1,0)

player_2_left = NoteButton(450,550,50,50,2,2)
player_2_down = NoteButton(510,550,50,50,2,1)
player_2_up = NoteButton(560,550,50,50,2,3)
player_2_right = NoteButton(610,550,50,50,2,0)
'''
p1_left_target = TargetNote(100,250,50,50,1,1)
p1_down_target = TargetNote(160,250,50,50,1,2)
p1_up_target = TargetNote(210,250,50,50,1,3)
p1_right_target = TargetNote(260,250,50,50,1,0)

p2_left_target = TargetNote(450,250,50,50,2,1)
p2_down_target = TargetNote(510,250,50,50,2,2)
p2_up_target = TargetNote(560,250,50,50,2,3)
p2_right_target = TargetNote(610,250,50,50,2,0)

player_1_list = []
player_2_list = []

song_length = len(loaded_song["tracks"][0])

next_note_location = []

def Button_check(beat,song_length,loaded_song):
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
        


running = True


while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # 0 = right, 2 = down, 1 = left, 3 = up
            
            #PLAYER 1
            if event.key == pygame.K_a:
                if player_1_list:
                    for note in player_1_list:
                        if note.button == 1 and note.visible == True:
                            print(f"p1 left: {p1_left_target.rect.y - note.rect.y}")

            if event.key == pygame.K_w:
                if player_1_list:
                    for note in player_1_list:
                        if note.button == 3 and note.visible == True:
                            print(f"p1 up: {p1_left_target.rect.y - note.rect.y}")

            if event.key == pygame.K_d:
                if player_1_list:
                    for note in player_1_list:
                        if note.button == 0 and note.visible == True:
                            print(f"p1 right: {p1_left_target.rect.y - note.rect.y}")
            if event.key == pygame.K_s:
                if player_1_list:
                    for note in player_1_list:
                        if note.button == 2 and note.visible == True:
                            print(f"p1 down: {p1_left_target.rect.y - note.rect.y}")
            
            #PLAYER 2 
            if event.key == pygame.K_LEFT:
                if player_2_list:
                    for note in player_2_list:
                        if note.button == 1 and note.visible == True:
                            print(f"p2 left: {p1_left_target.rect.y - note.rect.y}")
            if event.key == pygame.K_UP:
                if player_2_list:
                    for note in player_2_list:
                        if note.button == 3 and note.visible == True:
                            print(f"p2 up: {p1_left_target.rect.y - note.rect.y}")
            if event.key == pygame.K_RIGHT:
                if player_2_list:
                    for note in player_2_list:
                        if note.button == 0 and note.visible == True:
                            print(f"p2 right: {p1_left_target.rect.y - note.rect.y}")
            if event.key == pygame.K_DOWN:
                 if player_2_list:
                    for note in player_2_list:
                        if note.button == 2 and note.visible == True:
                            print(f"p2 down: {p1_left_target.rect.y - note.rect.y}")

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

    p1_left_target.draw() 
    p1_down_target.draw()
    p1_up_target.draw()
    p1_right_target.draw()

    p2_left_target.draw()
    p2_down_target.draw()
    p2_up_target.draw()
    p2_right_target.draw()



    if player_1_list:
        for note in player_1_list:
            note.draw()
            if note.rect.y <= 200:
                note.hide()

    if player_2_list:
        for note in player_2_list:
            note.draw()
            if note.rect.y <= 200:
                note.hide()

    
    pygame.display.flip()
    


pygame.quit()
sys.exit()