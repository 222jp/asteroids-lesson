import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, int(self.radius))

    def update(self, dt):
        self.position += (self.velocity * dt)
