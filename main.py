import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    player.cooldown = 0

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable,) 
    AsteroidField()

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

        for item in asteroids:
            if item.detect_collision(player):
                print("Game over!")
                return
            
        for item in asteroids:
            for bullet in shots:
                if item.detect_collision(bullet):
                    item.kill()
                    bullet.kill()


if __name__ == "__main__":
    main()