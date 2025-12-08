import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, float(self.radius), 2)

    def update(self, dt):
        self.pos += self.velocity * dt
