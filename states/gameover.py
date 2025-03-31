import pygame
from states.state import State
from utils.constants import GAMEOVER_OVERLAY, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverState(State):
    def __init__(self, game):
        super().__init__(game)
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.game.reset_game()
                self.game.change_state('PLAYING')
    
    def update(self):
        # No hay actualizaciones en el estado de Game Over
        pass
    
    def draw(self, surface):
        # Primero dibujamos el estado del juego congelado
        self.game.states['PLAYING'].draw(surface)
        
        # Overlay semitransparente rojo
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill(GAMEOVER_OVERLAY)
        surface.blit(overlay, (0, 0))
        
        # Textos de Game Over
        self._draw_text(surface, "GAME OVER", self.game.font_xlarge, WHITE, 
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        self._draw_text(surface, f"Tu Puntuación: {int(self.game.score)}", 
                       self.game.font_medium, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        if self.game.score == self.game.high_score:
            self._draw_text(surface, "¡Nuevo Récord!", self.game.font_medium, WHITE, 
                           SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
        else:
            self._draw_text(surface, f"Récord: {int(self.game.high_score)}", 
                           self.game.font_medium, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
        
        self._draw_text(surface, "Presiona [R] para Reiniciar", self.game.font_medium, WHITE, 
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75)
    
    def _draw_text(self, surface, text, font, color, center_x, center_y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(center_x, center_y))
        surface.blit(text_surface, text_rect)