from circleshape import *
from constants import *
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        super().__init__(x, y, radius)
                        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)


    def move(self, dt):
        self.position +=  (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_direction1 = pygame.math.Vector2.rotate(self.velocity, split_angle) * 1.2
            split_direction2 = pygame.math.Vector2.rotate(self.velocity, -split_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = split_direction1
            split2.velocity = split_direction2
