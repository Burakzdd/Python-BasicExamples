import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLUE = (0,0,255)

running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
     window.fill(WHITE)

     pygame.draw.rect(window, (255,0,0), (50, 50, 250, 250))
     pygame.draw.rect(window,BLUE,(150,150,250,250))
     pygame.draw.rect(window, (0,255,0), (250, 250, 250, 250))
     pygame.draw.ellipse(window, (0, 0, 0), (350, 350, 250, 250),20)
     pygame.display.update()



pygame.quit()
