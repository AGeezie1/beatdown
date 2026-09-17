import pygame

def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("smooth_operator.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

