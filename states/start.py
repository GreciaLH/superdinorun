import pygame
from states.state import State
from utils.constants import START_OVERLAY, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class StartState(State):
    def __init__(self, game):
        super().__init__(game)
        # Inicializar elementos específicos del estado de inicio
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                self.game.change_state('PLAYING')
    
    def update(self):
        # Actualizar elementos de fondo si es necesario
        pass
    
    def draw(self, surface):
        # Dibujar fondos
        self._draw_background(surface)
        
        # Overlay semitransparente
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill(START_OVERLAY)
        surface.blit(overlay, (0, 0))
        
        # Textos
        self._draw_text(surface, "PIXEL DINO RUN", self.game.font_large, WHITE, 
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        self._draw_text(surface, "Instrucciones:", self.game.font_medium, WHITE, 
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self._draw_text(surface, "Presiona [ESPACIO] o [FLECHA ARRIBA] para Saltar", 
                       self.game.font_small, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
        self._draw_text(surface, "¡Evita los Cactus!", self.game.font_small, WHITE, 
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70)
        self._draw_text(surface, "Presiona [ESPACIO] o [ENTER] para Empezar", 
                       self.game.font_medium, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75)
        
        # Dibujar dino estático
        self.game.states['PLAYING'].player.draw(surface)
    
    def _draw_background(self, surface):
        # Dibujar montañas
        for mountain in self.game.states['PLAYING'].mountains:
            mountain.draw(surface)
        
        # Dibujar nubes
        for cloud in self.game.states['PLAYING'].clouds:
            cloud.draw(surface)
        
        # Dibujar suelo principal
        pygame.draw.rect(surface, (210, 180, 140), 
                        (0, SCREEN_HEIGHT - 60, SCREEN_WIDTH, 60))
        
        # Dibujar textura del suelo
        for ground_tile in self.game.states['PLAYING'].ground_tiles:
            ground_tile.draw(surface)
    
    def _draw_text(self, surface, text, font, color, center_x, center_y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(center_x, center_y))
        surface.blit(text_surface, text_rect)