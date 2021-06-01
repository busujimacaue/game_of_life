import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

running = True

is_blue = True

toroide = False

x = 0
y = 0

while running:
    
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    press=pygame.key.get_pressed()
    if pygame.key.get_pressed()[pygame.K_UP]: y -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]: y += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]: x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]: x += 5
    

    pygame.draw.rect(screen, RED, pygame.Rect(x, y, 50, 50))
        
    
    pygame.display.flip()
    clock.tick(60)

#teste
