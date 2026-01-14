import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):

    def draw(self, screen_object):
        pygame.draw.circle(screen_object, pygame.Color('white'), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt