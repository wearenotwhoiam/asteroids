import pygame
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    

    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroidField = AsteroidField()
    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updatables:
            u.update(dt)
        screen.fill((0))
        for d in drawables:
            d.draw(screen)
        for a in asteroids:
            if(a.checkcollision(player)):
                print("Game Over!")
                exit()
            for s in shots:
                if(a.checkcollision(s)):
                    a.split()
                    s.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()