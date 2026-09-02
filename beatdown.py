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

keys = pygame.key.getpressed()


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT")
            if event.key == pygame.K_UP:
                print("UP")
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
            if event.key == pygame.K_DOWN:
                print("DOWN")

            if event.key == pygame.K_a:
                print("LEFT")
            if event.key == pygame.K_w:
                print("UP")
            if event.key == pygame.K_d:
                print("RIGHT")
            if event.key == pygame.K_s:
                print("DOWN")
            

            


    screen.fill((0, 0, 0)) 
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
