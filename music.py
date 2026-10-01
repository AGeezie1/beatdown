import pygame

def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("smooth_operator.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

