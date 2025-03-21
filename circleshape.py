import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, cs_obj):
        return self.position.distance_to(cs_obj.position) <= self.radius + cs_obj.radius
        # distance = pygame.math.Vector2.distance_to(self.position, cs_obj.position)
        # if (self.radius + cs_obj.radius) >= distance:
        #     return True
        # return False
    
    # def check_screen_border_collision(self, cs_obj):
    #     screen_rect = pygame.display.get_surface().get_rect()

    #     if screen_rect.contains(cs_obj.x , cs_obj.y):
            