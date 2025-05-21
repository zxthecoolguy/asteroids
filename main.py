import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shootingpowerup import ShootingPowerup
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    powerups = pygame.sprite.Group()
    ShootingPowerup.containers = (powerups, updatable, drawable)

    last_powerup_spawn = 0

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
            
        for asteroid1 in asteroids:
            for asteroid2 in asteroids:
                if asteroid1 is not asteroid2 and asteroid1.collides_with(asteroid2):
                    asteroid1.split()

        for powerup in powerups:
            if powerup.collides_with(player):
                player.shooting_powerup()
                powerup.kill()

        if pygame.time.get_ticks() / 1000 - last_powerup_spawn >= POWERUP_SPAWN_RATE:
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            ShootingPowerup(x, y)
            last_powerup_spawn = pygame.time.get_ticks() / 1000

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
