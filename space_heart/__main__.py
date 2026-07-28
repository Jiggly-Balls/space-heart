import pygame


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Space Heart")
    window = pygame.display.set_mode((640, 360))


if __name__ == "__main__":
    main()
    pygame.quit()
