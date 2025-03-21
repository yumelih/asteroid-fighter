import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.has_entered_screen = False
        self.alive_time = 0
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, radius=self.radius, color=(255, 255, 255), width=2, center=self.position)

    def update(self, dt, screen_rect):
        self.position += self.velocity * dt
        self.alive_time += dt

        if self.alive_time > 10 and not self.has_entered_screen:
            self.kill()

        if not self.has_entered_screen:
            if (screen_rect.left + self.radius <= self.position.x <= screen_rect.right - self.radius and
            screen_rect.top + self.radius <= self.position.y <= screen_rect.bottom - self.radius):
                self.has_entered_screen = True

        if self.has_entered_screen:
            if self.position.x - self.radius <= screen_rect.left or self.position.x + self.radius >= screen_rect.right:
                self.velocity.x *= -1
            if self.position.y - self.radius <= screen_rect.top or self.position.y + self.radius >= screen_rect.bottom:
                self.velocity.y *= -1

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(random_angle)
        new_vel_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = new_vel_1 * 1.2
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2.velocity = new_vel_2 * 1.2

        
