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

    def collides_with(self, other):
        distance_between_centers = self.position.distance_to(other.position)
        colision_distance = self.radius + other.radius
        if distance_between_centers <= colision_distance:
            return True

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
