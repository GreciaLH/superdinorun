import pygame
import random
from states.state import State
from sprites.player import Player
from sprites.obstacle import Obstacle
from sprites.background import BackgroundElement
from utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT, 
                           GROUND_BROWN, SKY_BLUE, TEXT_COLOR, CLOUD_SPRITE_DATA,
                           MOUNTAIN_SPRITE_DATA, SPAWN_RATE, MIN_SPAWN_RATE,
                           SPEED_INCREASE_FACTOR)

class PlayingState(State):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(SCREEN_WIDTH * 0.2)
        self.obstacles = []
        self.clouds = []
        self.mountains = []
        self.ground_tiles = []
        self.obstacle_timer = 0
        self.spawn_rate = SPAWN_RATE
        
        # Inicializar elementos de fondo
        self._init_background_elements()
    
    def _init_background_elements(self):
        # Crear nubes
        for _ in range(5):
            self.clouds.append(
                BackgroundElement(
                    random.uniform(0, SCREEN_WIDTH),
                    random.uniform(50, SCREEN_HEIGHT * 0.4),
                    0.5,
                    CLOUD_SPRITE_DATA,
                    'cloud',
                    self.game.game_speed
                )
            )
        
        # Crear montañas
        for _ in range(3):
            self.mountains.append(
                BackgroundElement(
                    random.uniform(0, SCREEN_WIDTH * 1.5),
                    GROUND_HEIGHT,
                    0.2,
                    MOUNTAIN_SPRITE_DATA,
                    'mountain',
                    self.game.game_speed
                )
            )
        
        # Crear tiles del suelo
        for i in range(int(SCREEN_WIDTH / 40) + 2):
            self.ground_tiles.append(
                BackgroundElement(
                    i * 40,
                    0,
                    1.0,
                    None,
                    'ground',
                    self.game.game_speed
                )
            )
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                self.player.jump()
    
    def update(self):
        # Actualizar jugador
        self.player.update()
        
        # Actualizar obstáculos
        self._update_obstacles()
        
        # Actualizar elementos de fondo
        self._update_background()
        
        # Actualizar puntuación y velocidad
        self.game.score += 0.15
        self.game.game_speed += SPEED_INCREASE_FACTOR
        
        # Actualizar velocidad de los elementos
        self._update_element_speeds()
    
    def _update_obstacles(self):
        self.obstacle_timer += 1
        if self.obstacle_timer >= self.spawn_rate:
            self.obstacle_timer = 0
            self.obstacles.append(Obstacle(self.game.game_speed))
            # Reducir spawn rate gradualmente
            if self.spawn_rate > MIN_SPAWN_RATE:
                self.spawn_rate -= 0.5
            
            # Añadir variación aleatoria al próximo intervalo de generación
            # Esto hará que la distancia entre obstáculos varíe
            random_variation = random.uniform(-15, 15)
            self.spawn_rate = max(MIN_SPAWN_RATE, min(SPAWN_RATE, self.spawn_rate + random_variation))
        
        # Mover y eliminar obstáculos
        for i in range(len(self.obstacles) - 1, -1, -1):
            obs = self.obstacles[i]
            obs.update()
            if obs.is_offscreen():
                self.obstacles.pop(i)
            elif self.player.rect.colliderect(obs.rect):
                self._handle_collision()
    
    def _handle_collision(self):
        if self.game.score > self.game.high_score:
            self.game.high_score = self.game.score
        self.game.change_state('GAME_OVER')
    
    def _update_background(self):
        for bg_element in self.clouds + self.mountains + self.ground_tiles:
            bg_element.update()
    
    def _update_element_speeds(self):
        for element in self.obstacles + self.clouds + self.mountains + self.ground_tiles:
            element.game_speed = self.game.game_speed
    
    def draw(self, surface):
        # Fondo base
        surface.fill(SKY_BLUE)
        
        # Dibujar montañas
        for mountain in self.mountains:
            mountain.draw(surface)
        
        # Dibujar nubes
        for cloud in self.clouds:
            cloud.draw(surface)
        
        # Dibujar suelo principal
        pygame.draw.rect(surface, GROUND_BROWN, 
                        (0, GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))
        
        # Dibujar textura del suelo
        for ground_tile in self.ground_tiles:
            ground_tile.draw(surface)
        
        # Dibujar jugador
        self.player.draw(surface)
        
        # Dibujar obstáculos
        for obstacle in self.obstacles:
            obstacle.draw(surface)
        
        # Dibujar puntuación
        self._draw_text_topleft(surface, f"Score: {int(self.game.score)}", 
                              self.game.font_small, TEXT_COLOR, 20, 20)
        self._draw_text_topleft(surface, f"Hi: {int(self.game.high_score)}", 
                              self.game.font_small, TEXT_COLOR, 20, 50)
    
    def _draw_text_topleft(self, surface, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(topleft=(x, y))
        surface.blit(text_surface, text_rect)
    
    def reset(self):
        self.player = Player(SCREEN_WIDTH * 0.2)
        self.obstacles = []
        self.obstacle_timer = 0
        self.spawn_rate = SPAWN_RATE