import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        self.velocity = PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "grey", self.position, self.radius, width=0)

    def update(self, dt):
        self.position += (self.velocity * dt)