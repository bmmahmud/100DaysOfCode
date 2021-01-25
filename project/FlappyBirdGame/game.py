import pygame

pygame.init()

screen = pygame.display.set_mode((288,512))

# main Loop
running = True
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

