import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_one = Asteroid(
                self.position[0], self.position[1], split_asteroid_radius
            )
            split_asteroid_two = Asteroid(
                self.position[0], self.position[1], split_asteroid_radius
            )
            split_asteroid_one.velocity = self.velocity.rotate(split_angle) * 1.2
            split_asteroid_two.velocity = self.velocity.rotate(-split_angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
