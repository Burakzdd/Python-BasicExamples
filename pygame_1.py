import pygame

pygame.init()
Pencere = (800,600)
pygame.display.set_mode(Pencere)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)


pygame.quit()
