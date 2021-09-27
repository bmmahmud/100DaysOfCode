import pygame

def game_build():
    pygame.init()
    window = pygame.display.set_mode((288, 510))

    # Background
    bkg_img = pygame.image.load("assets/bg.png")

    # main Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Game Logic
    window.blit(bkg_img, (0, 0))

    # Updating
    clock.tick(60)
    pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_build()

