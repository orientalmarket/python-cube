import pygame
import numpy as np

colors = {"white": (0, 0, 0), "black": (255, 255, 255)}


def main():
    pygame.init()
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("3D Cube")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        clock.tick(60)
        screen.fill(colors["white"])

    pygame.quit()


if __name__ == "__main__":
    main()
