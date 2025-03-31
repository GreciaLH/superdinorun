import pygame
from utils.constants import CACTUS_SPRITE_DATA, SCREEN_WIDTH, GROUND_HEIGHT

class Obstacle:
    def __init__(self, game_speed):
        self.sprite_data = CACTUS_SPRITE_DATA
        self.width = self.sprite_data['width']
        self.height = self.sprite_data['height']
        # Posición es centro inferior
        self.x = SCREEN_WIDTH + self.width / 2
        self.y = GROUND_HEIGHT
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = (self.x, self.y)
        self.game_speed = game_speed

    def update(self):
        self.x -= self.game_speed
        self.rect.midbottom = (self.x, self.y)

    def draw(self, surface):
        # Usamos midbottom como referencia
        mid_bottom_x, mid_bottom_y = self.rect.midbottom

        # Base
        base_pos, base_size = self.sprite_data['base']
        base_rect = pygame.Rect(0, 0, base_size[0], base_size[1])
        base_rect.midbottom = (mid_bottom_x + base_pos[0], 
                              mid_bottom_y + base_pos[1] + base_size[1])
        pygame.draw.rect(surface, self.sprite_data['color'], base_rect)

        # Brazo 1
        arm1_pos, arm1_size = self.sprite_data['arm1']
        arm1_rect = pygame.Rect(0, 0, arm1_size[0], arm1_size[1])
        arm1_rect.midbottom = (mid_bottom_x + arm1_pos[0], 
                              mid_bottom_y + arm1_pos[1] + arm1_size[1])
        pygame.draw.rect(surface, self.sprite_data['color'], arm1_rect)

        # Brazo 2
        arm2_pos, arm2_size = self.sprite_data['arm2']
        arm2_rect = pygame.Rect(0, 0, arm2_size[0], arm2_size[1])
        arm2_rect.midbottom = (mid_bottom_x + arm2_pos[0], 
                              mid_bottom_y + arm2_pos[1] + arm2_size[1])
        pygame.draw.rect(surface, self.sprite_data['color'], arm2_rect)

    def is_offscreen(self):
        return self.rect.right < 0