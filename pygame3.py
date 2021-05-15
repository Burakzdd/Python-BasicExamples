import pygame

pygame.init()
Pencere = (800,600)
window = pygame.display.set_mode(Pencere)

R = G = B = 0


running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if R<255:
                    R=R+20
            if event.key == pygame.K_g:
                if G<255:
                    G=G+20
            if event.key == pygame.K_b:
                if B<255:
                    B=B+20
        window.fill((R,G,B))
        pygame.display.update()



pygame.quit()