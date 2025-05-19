import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other_shape):
        # Calculate the distance between the centers
        distance = self.position.distance_to(other_shape.position)
        
        # Get the sum of the radii
        radii_sum = self.radius + other_shape.radius
        
        # Collision happens when distance <= sum of radii
        return distance <= radii_sum