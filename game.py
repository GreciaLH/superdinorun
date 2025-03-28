import pygame
import sys
from utils.constants import *
from states.start import StartState
from states.playing import PlayingState
from states.gameover import GameOverState

class Game:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()
        
        # Configuración de la pantalla
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Dino Run")
        self.clock = pygame.time.Clock()
        
        # Puntuación
        self.score = 0
        self.high_score = 0
        
        # Velocidad del juego - Inicializar antes de crear los estados
        self.game_speed = INITIAL_GAME_SPEED
        
        # Estados del juego
        self.states = {
            'START': StartState(self),
            'PLAYING': PlayingState(self),
            'GAME_OVER': GameOverState(self)
        }
        self.current_state = 'START'
        
        # Cargar fuentes
        self.load_fonts()
    
    def load_fonts(self):
        try:
            self.font_small = pygame.font.SysFont('monospace', 24)
            self.font_medium = pygame.font.SysFont('monospace', 32)
            self.font_large = pygame.font.SysFont('monospace', 48)
            self.font_xlarge = pygame.font.SysFont('monospace', 60)
        except:
            print("Fuente 'monospace' no encontrada, usando fuente por defecto.")
            self.font_small = pygame.font.Font(None, 24)
            self.font_medium = pygame.font.Font(None, 32)
            self.font_large = pygame.font.Font(None, 48)
            self.font_xlarge = pygame.font.Font(None, 60)
    
    def change_state(self, new_state):
        self.current_state = new_state
    
    def reset_game(self):
        self.score = 0
        self.game_speed = INITIAL_GAME_SPEED
        self.states['PLAYING'].reset()
    
    def run(self):
        running = True
        while running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Pasar eventos al estado actual
                self.states[self.current_state].handle_events(event)
            
            # Actualizar estado actual
            self.states[self.current_state].update()
            
            # Dibujar estado actual
            self.screen.fill(SKY_BLUE)
            self.states[self.current_state].draw(self.screen)
            
            # Actualizar pantalla
            pygame.display.flip()
            
            # Controlar FPS
            self.clock.tick(FPS)