import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # containers is a special property that keeps track of the sprite that is made and updates group depending on the groups that object belongs to. We decide a class groups with containers property.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    # player will automatically added to the updatable and drawable because of the line above
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
  
    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if(asteroid.check_collision(player)):
                print('Game over!')
                sys.exit()

            for shot in shots:
                if(shot.check_collision(asteroid)):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen=screen)
        
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

        # player.update(dt)
        # player.draw(screen=screen)


    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
    main()