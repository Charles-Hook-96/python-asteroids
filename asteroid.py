import pygame.draw

from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen_object):
        pygame.draw.circle(screen_object, pygame.Color('white'), self.position, self.radius, LINE_WIDTH)