import pygame
import random
from utils.constants import (CLOUD_SPRITE_DATA, MOUNTAIN_SPRITE_DATA, 
                           SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT)

class BackgroundElement:
    def __init__(self, x, y, speed_factor, sprite_data, element_type, game_speed):
        self.x = x
        self.y = y
        self.speed_factor = speed_factor
        self.sprite_data = sprite_data
        self.type = element_type
        self.rect = None  # Rectángulo para dibujar/posicionar
        self.game_speed = game_speed

        if self.type == 'mountain':
            self._init_mountain()
        elif self.type == 'cloud':
            self._init_cloud()
        elif self.type == 'ground':
            self._init_ground()

    def _init_mountain(self):
        self.base_width = self.sprite_data['base_width'] + random.uniform(-50, 50)
        self.m_height = self.sprite_data['height'] + random.uniform(-40, 40)
        self.y = GROUND_HEIGHT  # Anclar al suelo
        # Puntos del triángulo principal
        self.points = [
            (self.x - self.base_width / 2, self.y),
            (self.x + self.base_width / 2, self.y),
            (self.x, self.y - self.m_height)
        ]
        # Puntos del pico nevado
        cap_width_factor = 0.3
        self.cap_points = [
            (self.x - self.base_width / 2 * cap_width_factor, self.y - self.m_height * 0.6),
            (self.x + self.base_width / 2 * cap_width_factor, self.y - self.m_height * 0.6),
            (self.x, self.y - self.m_height)
        ]

    def _init_cloud(self):
        # Crear una superficie para la nube para manejar la transparencia
        max_w = max(p['x'] + p['w'] for p in self.sprite_data['parts']) - min(p['x'] for p in self.sprite_data['parts'])
        max_h = max(p['y'] + p['h'] for p in self.sprite_data['parts']) - min(p['y'] for p in self.sprite_data['parts'])
        self.surface = pygame.Surface((max_w+10, max_h+10), pygame.SRCALPHA)  # +10 margen
        self.surface.fill((0,0,0,0))  # Transparente por defecto
        base_x = -min(p['x'] for p in self.sprite_data['parts']) + 5
        base_y = -min(p['y'] for p in self.sprite_data['parts']) + 5
        color = self.sprite_data['color']
        for part in self.sprite_data['parts']:
            pygame.draw.rect(self.surface, color, (base_x + part['x'], base_y + part['y'], part['w'], part['h']))
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def _init_ground(self):
        self.color = (180 + random.randint(-10, 10),
                      150 + random.randint(-10, 10),
                      110 + random.randint(-10, 10))
        self.w = 40
        self.h = 10 + random.uniform(0, 15)
        self.y = GROUND_HEIGHT + (60 - self.h)  # Posicionar desde el suelo visual
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.x -= self.game_speed * self.speed_factor

        # Lógica de envolvimiento (wrap around)
        if self.type == 'cloud':
            self._update_cloud()
        elif self.type == 'mountain':
            self._update_mountain()
        elif self.type == 'ground':
            self._update_ground()

    def _update_cloud(self):
        self.rect.x = self.x
        if self.rect.right < 0:
            self.x = SCREEN_WIDTH + random.uniform(50, 150)
            self.y = random.uniform(50, SCREEN_HEIGHT * 0.4)
            self.rect.topleft = (self.x, self.y)

    def _update_mountain(self):
        # Actualizar puntos basados en la nueva x
        self.points = [(p[0] - self.game_speed * self.speed_factor, p[1]) for p in self.points]
        self.cap_points = [(p[0] - self.game_speed * self.speed_factor, p[1]) for p in self.cap_points]
        # La 'x' lógica también se mueve
        self.x -= self.game_speed * self.speed_factor
        # Comprobar si el punto más a la derecha está fuera de pantalla
        if self.x + self.base_width / 2 < 0:
            self.x = SCREEN_WIDTH + self.base_width / 2 + random.uniform(0, self.base_width)
            self.base_width = self.sprite_data['base_width'] + random.uniform(-50, 50)
            self.m_height = self.sprite_data['height'] + random.uniform(-40, 40)
            self.y = GROUND_HEIGHT
            # Recalcular puntos
            self._init_mountain()

    def _update_ground(self):
        self.rect.x = self.x
        if self.rect.right < 0:
            self.x = SCREEN_WIDTH  # Aparecer justo al salir
            self.rect.left = self.x

    def draw(self, surface):
        if self.type == 'cloud' and self.rect:
            surface.blit(self.surface, self.rect)
        elif self.type == 'mountain':
            pygame.draw.polygon(surface, self.sprite_data['color1'], self.points)
            pygame.draw.polygon(surface, self.sprite_data['color2'], self.cap_points)
        elif self.type == 'ground' and self.rect:
            pygame.draw.rect(surface, self.color, self.rect)