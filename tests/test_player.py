import unittest
import pygame
import sys
import os

# Añadir el directorio raíz al path para poder importar los módulos del juego
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sprites.player import Player
from utils.constants import GROUND_HEIGHT, JUMP_FORCE

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Inicializar pygame para los tests
        pygame.init()
        # Crear una instancia de Player para cada test
        self.player = Player(100)
    
    def tearDown(self):
        # Limpiar después de cada test
        pygame.quit()
    
    def test_player_initialization(self):
        """Test que verifica la correcta inicialización del jugador."""
        self.assertEqual(self.player.x, 100)
        self.assertTrue(self.player.on_ground)
        self.assertEqual(self.player.vy, 0)
    
    def test_player_jump(self):
        """Test que verifica que el jugador salta correctamente."""
        # El jugador comienza en el suelo
        self.assertTrue(self.player.on_ground)
        
        # Hacer que el jugador salte
        self.player.jump()
        
        # Verificar que ya no está en el suelo y que tiene velocidad vertical negativa
        self.assertFalse(self.player.on_ground)
        self.assertEqual(self.player.vy, JUMP_FORCE)
    
    def test_player_update(self):
        """Test que verifica la actualización de la posición del jugador."""
        initial_y = self.player.y
        
        # Hacer que el jugador salte
        self.player.jump()
        
        # Actualizar la posición
        self.player.update()
        
        # Verificar que la posición Y ha cambiado
        self.assertNotEqual(self.player.y, initial_y)
    
    def test_player_gravity(self):
        """Test que verifica que la gravedad afecta al jugador."""
        # Hacer que el jugador salte
        self.player.jump()
        
        # Guardar la velocidad vertical inicial
        initial_vy = self.player.vy
        
        # Actualizar la posición
        self.player.update()
        
        # Verificar que la velocidad vertical ha aumentado (gravedad positiva)
        self.assertGreater(self.player.vy, initial_vy)
    
    def test_player_ground_collision(self):
        """Test que verifica que el jugador no puede caer por debajo del suelo."""
        # Forzar al jugador a estar por encima del suelo
        self.player.y = GROUND_HEIGHT - 100
        self.player.on_ground = False
        self.player.vy = 10  # Velocidad hacia abajo
        
        # Actualizar varias veces para asegurar que llega al suelo
        for _ in range(20):
            self.player.update()
        
        # Verificar que el jugador está en el suelo y no ha caído por debajo
        self.assertTrue(self.player.on_ground)
        self.assertEqual(self.player.vy, 0)
        self.assertLessEqual(self.player.y, GROUND_HEIGHT)

if __name__ == '__main__':
    unittest.main()