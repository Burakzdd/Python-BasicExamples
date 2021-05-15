import pygame

pygame.init()
Pencere = (800,600)
window = pygame.display.set_mode(Pencere)

renk = (56,89,255)


running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        window.fill(renk)
        pygame.display.flip()
        print(event)


pygame.quit()
