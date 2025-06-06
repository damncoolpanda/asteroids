import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
SCORE_FONT = pygame.font.SysFont('Verdana', 30)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), display=1)
dt = 0
clock = pygame.time.Clock()
FPS = 60

#screen.blit(SCORE_FONT.render(str(Score), True, (255, 0, 0)), (SCREEN_WIDTH-200, 20))

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Score = 0
    print('Score: ' + str(Score))


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
        screen.blit(SCORE_FONT.render(str(Score), True, (0, 255, 0)), (SCREEN_WIDTH-100, 20))

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                return

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.detect_collision(bullet):
                    Score += 100
                    print('Score: ' + str(Score))
                    asteroid.split()
                    bullet.kill()

if __name__ == "__main__":
    main()