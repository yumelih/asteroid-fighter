import pygame
from constants import SCORE_FONT

class Score():
    def __init__(self, font_size, font_color = (173, 128, 3)):
        self.font = pygame.font.SysFont(SCORE_FONT, font_size)
        self.font_color = font_color
        self.score = 0

    def update_score(self, points, multiplier = 1):
        self.score += (points * multiplier)

    def render_score(self, screen):
        text_surface = self.font.render(f"Score: {self.score}", False, self.font_color)
        screen.blit(text_surface, (0,0))