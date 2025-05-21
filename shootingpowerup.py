from circleshape import CircleShape
from constants import POWERUP_RADIUS
import pygame
import math
import time

class ShootingPowerup(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.color = (255, 0, 0)
        self.base_y = y  # For floating effect

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Simple float animation
        self.position.y = self.base_y + math.sin(pygame.time.get_ticks() * 0.005) * 5
