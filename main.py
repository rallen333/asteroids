import pygame
import sys
from constants import *
from player import *
from asteroids import Asteroid
from asteroidfield import *
from circleshape import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in updatable:
            sprite.update(dt)
        for item in drawable:
            item.draw(screen)
        for shot in shots:
            shot.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
        

if __name__ == "__main__":
    main()