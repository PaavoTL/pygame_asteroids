import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shot_timer = 0.0
  
  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
    
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
    
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.velocity += forward * PLAYER_SPEED * dt
  
  def shoot(self):
    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    self.shot_timer = PLAYER_SHOOT_COOLDOWN
    
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(),2)
    
  def update(self, dt):
    keys = pygame.key.get_pressed()
    self.position += self.velocity * dt

    if keys[pygame.K_a]:
      self.rotate(dt*-1)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(dt*-1)
    
    self.shot_timer -= dt
    if keys[pygame.K_SPACE]:
      if self.shot_timer < 0:
        self.shoot()