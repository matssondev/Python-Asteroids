import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.pos += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        roid1 = self.velocity.rotate(angle)
        roid2 = self.velocity.rotate(-angle)

        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.pos.x, self.pos.y, new_radius)
        asteroid.velocity = roid1 * 1.2
        asteroid = Asteroid(self.pos.x, self.pos.y, new_radius)
        asteroid.velocity = roid2 * 1.2
