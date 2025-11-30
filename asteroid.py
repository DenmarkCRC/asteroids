import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(split_angle)
        new_vector2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2


    def shoot(self):
        if self.shot_cool_down_time <= 0:
            self.shot_cool_down_time = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
            shot.velocity = rotated_with_speed_vector        
