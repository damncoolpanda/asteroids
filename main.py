import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), display=1)
dt = 0
clock = pygame.time.Clock()
FPS = 60

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        updatable.update(dt)



if __name__ == "__main__":
    main()