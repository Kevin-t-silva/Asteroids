import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 30)
            self.velocity1 = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            self.velocity2 = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = self.velocity1 * 1.2
            asteroid2.velocity = self.velocity2 * 1.2
