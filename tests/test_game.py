import unittest
import pygame
import sys
import os

# Añadir el directorio raíz al path para poder importar los módulos del juego
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import Game
from utils.constants import INITIAL_GAME_SPEED

class TestGame(unittest.TestCase):
    def setUp(self):
        # Inicializar pygame para los tests
        pygame.init()
        # Crear una instancia de Game para cada test
        self.game = Game()
    
    def tearDown(self):
        # Limpiar después de cada test
        pygame.quit()
    
    def test_game_initialization(self):
        """Test que verifica la correcta inicialización del juego."""
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.high_score, 0)
        self.assertEqual(self.game.game_speed, INITIAL_GAME_SPEED)
        self.assertEqual(self.game.current_state, 'START')
        self.assertIn('START', self.game.states)
        self.assertIn('PLAYING', self.game.states)
        self.assertIn('GAME_OVER', self.game.states)
    
    def test_game_change_state(self):
        """Test que verifica el cambio de estado del juego."""
        # El estado inicial es 'START'
        self.assertEqual(self.game.current_state, 'START')
        
        # Cambiar al estado 'PLAYING'
        self.game.change_state('PLAYING')
        self.assertEqual(self.game.current_state, 'PLAYING')
        
        # Cambiar al estado 'GAME_OVER'
        self.game.change_state('GAME_OVER')
        self.assertEqual(self.game.current_state, 'GAME_OVER')
    
    def test_game_reset(self):
        """Test que verifica el reinicio del juego."""
        # Modificar algunos valores
        self.game.score = 100
        self.game.game_speed = 20
        
        # Reiniciar el juego
        self.game.reset_game()
        
        # Verificar que los valores se han reiniciado
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.game_speed, INITIAL_GAME_SPEED)

if __name__ == '__main__':
    unittest.main()