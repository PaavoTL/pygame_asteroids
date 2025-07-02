import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.rotation = 0
    self.rotation_speed = random.uniform(-100,100)
    self.shape_points = []
    for i in range (0,18):
      self.shape_points.append(random.uniform(0, radius/5))
    
      
  def chunky(self):
    result_points = []
    segment = 360 / len(self.shape_points)
    for i in range(0, len(self.shape_points)):
      point_position = pygame.Vector2(0, self.radius + self.shape_points[i]).rotate(self.rotation + segment * i)
      result_points.append(self.position + point_position)
    return result_points
  
  def draw(self, screen):
    points = self.chunky()
    
    #pygame.draw.circle(screen, "black", self.position, self.radius)
    #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    pygame.draw.polygon(screen, "black", points)
    pygame.draw.polygon(screen, "white", points, 2)
    
    
  def update(self, dt):
    self.position += self.velocity * dt
    self.rotation += self.rotation_speed * dt
    
  def split (self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(20,50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    velocity1 = self.velocity.rotate(angle)
    velocity2 = self.velocity.rotate(-angle)
    
    
    asteroid1 = Asteroid(self.position.x , self.position.y, new_radius)
    asteroid1.velocity = velocity1 * 1.2
    
    asteroid2 = Asteroid(self.position.x , self.position.y, new_radius)
    asteroid2.velocity = velocity2 * 1.2