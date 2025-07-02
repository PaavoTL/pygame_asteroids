import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)
  
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
    
  while True:
    #Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for item in updatable:
      item.update(dt)
        
    for asteroid in asteroids:
      if asteroid.collide_with_circle(player):
        print("Game over!")
        return
      
      for shot in shots:
        if asteroid.collide_with_circle(shot):
          asteroid.split()
          shot.kill()
        
            
    
    #Draw
    screen.fill("black")
    
    for item in drawable:
      item.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()
