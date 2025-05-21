import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0.0
        self.shoot_speed = PLAYER_SHOOT_SPEED
        self.powerup = False
        self.powerup_timer = POWERUP_TIME
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if self.powerup:
            self.powerup_timer -= dt
            if self.powerup_timer <= 0:
                self.shooting_powerup_end()
                self.powerup = False
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * self.shoot_speed
            self.timer = self.shoot_cooldown  # <-- use the variable!

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shooting_powerup(self):
        self.powerup_timer = POWERUP_TIME
        self.powerup = True
        self.shoot_speed *= 2
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN / 4

    def shooting_powerup_end(self):
        self.shoot_speed = PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

