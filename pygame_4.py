import pygame

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("ADAM")
WHITE = (255,255,255)

manImg = pygame.image.load('man.jpg')
manx = 10
many = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        manx =manx+ 5
        if manx == 280:
          direction = 'down'
    elif direction == 'down':
        many =many+ 5
        if many == 200:
            direction = 'left'
    elif direction == 'left':
        manx= manx-5
        if manx == 28:
            direction = 'up'
    elif direction == 'up':
        many=many - 5
        if many==200:
            direction = 'right'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    DISPLAYSURF.blit(manImg,(manx,many))
    pygame.display.update()
    fpsClock.tick(FPS)


pygame.quit()
