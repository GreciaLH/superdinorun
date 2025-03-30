import pygame
from utils.constants import DINO_SPRITE_DATA, GRAVITY, JUMP_FORCE, GROUND_HEIGHT

class Player:
    def __init__(self, x_pos):
        self.sprite_data = DINO_SPRITE_DATA
        # Posición central del dinosaurio
        self.x = x_pos
        self.y = GROUND_HEIGHT - self.sprite_data['height'] / 2
        self.vy = 0  # Velocidad vertical
        self.width = self.sprite_data['width']
        self.height = self.sprite_data['height']
        # Rectángulo de colisión
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_FORCE
            self.on_ground = False

    def update(self):
        self.vy += GRAVITY
        self.y += self.vy

        # Revisar si está en el suelo
        ground_level = GROUND_HEIGHT - self.height / 2
        if self.y >= ground_level:
            self.y = ground_level
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # Actualizar la posición del rectángulo de colisión
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        # Usamos el centro del rect como punto de referencia para dibujar las partes
        center_x, center_y = self.rect.center

        # Dibujar Cuerpo
        body_pos, body_size = self.sprite_data['body']
        body_rect = pygame.Rect(0, 0, body_size[0], body_size[1])
        body_rect.center = (center_x + body_pos[0], center_y + body_pos[1])
        pygame.draw.rect(surface, self.sprite_data['color'], body_rect)

        # Dibujar Cabeza
        head_pos, head_size = self.sprite_data['head']
        head_rect = pygame.Rect(0, 0, head_size[0], head_size[1])
        head_rect.center = (center_x + head_pos[0], center_y + head_pos[1])
        pygame.draw.rect(surface, self.sprite_data['color'], head_rect)

        # Dibujar Cola
        tail_pos, tail_size = self.sprite_data['tail']
        tail_rect = pygame.Rect(0, 0, tail_size[0], tail_size[1])
        tail_rect.center = (center_x + tail_pos[0], center_y + tail_pos[1])
        pygame.draw.rect(surface, self.sprite_data['color'], tail_rect)

        # Dibujar Piernas (animación simple)
        leg_offset = 4 if (pygame.time.get_ticks() // 100) % 2 == 0 else 0
        
        leg1_pos, leg1_size = self.sprite_data['leg1']
        leg1_rect = pygame.Rect(0, 0, leg1_size[0], leg1_size[1])
        leg1_rect.midbottom = (center_x + leg1_pos[0] + leg1_size[0]/2, 
                              center_y + self.height/2 + leg_offset / 2)
        pygame.draw.rect(surface, self.sprite_data['color'], leg1_rect)

        leg2_pos, leg2_size = self.sprite_data['leg2']
        leg2_rect = pygame.Rect(0, 0, leg2_size[0], leg2_size[1])
        leg2_rect.midbottom = (center_x + leg2_pos[0] + leg2_size[0]/2, 
                              center_y + self.height/2 - leg_offset / 2)
        pygame.draw.rect(surface, self.sprite_data['color'], leg2_rect)

        # Dibujar Ojo
        eye_pos, eye_size = self.sprite_data['eye']
        eye_rect = pygame.Rect(0, 0, eye_size[0], eye_size[1])
        eye_rect.center = (center_x + eye_pos[0], center_y + eye_pos[1])
        pygame.draw.rect(surface, self.sprite_data['eye_color'], eye_rect)