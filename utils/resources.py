import pygame

def draw_text(surface, text, font, color, center_x, center_y):
    """Dibuja texto centrado en las coordenadas especificadas."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    surface.blit(text_surface, text_rect)

def draw_text_topleft(surface, text, font, color, x, y):
    """Dibuja texto alineado a la esquina superior izquierda."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    surface.blit(text_surface, text_rect)