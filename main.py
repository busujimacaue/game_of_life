import pygame
print(pygame.ver)
pygame.init()


BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")
pygame.display('teste')

running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


#teste