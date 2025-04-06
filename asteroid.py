import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "grey", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            new_velocity_1 = self.velocity.rotate(new_angle)
            new_velocity_2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius-ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(*self.position, new_radius)
            asteroid2 = Asteroid(*self.position, new_radius)
            asteroid1.velocity = new_velocity_1 * 1.2
            asteroid2.velocity = new_velocity_2 * 1.2

