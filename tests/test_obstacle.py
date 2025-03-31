import unittest
import pygame
import sys
import os

# Añadir el directorio raíz al path para poder importar los módulos del juego
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sprites.obstacle import Obstacle
from utils.constants import SCREEN_WIDTH, GROUND_HEIGHT

class TestObstacle(unittest.TestCase):
    def setUp(self):
        # Inicializar pygame para los tests
        pygame.init()
        # Crear una instancia de Obstacle para cada test
        self.game_speed = 5.0
        self.obstacle = Obstacle(self.game_speed)
    
    def tearDown(self):
        # Limpiar después de cada test
        pygame.quit()
    
    def test_obstacle_initialization(self):
        """Test que verifica la correcta inicialización del obstáculo."""
        self.assertGreater(self.obstacle.x, SCREEN_WIDTH)
        self.assertEqual(self.obstacle.y, GROUND_HEIGHT)
        self.assertEqual(self.obstacle.game_speed, self.game_speed)
    
    def test_obstacle_update(self):
        """Test que verifica que el obstáculo se mueve correctamente."""
        initial_x = self.obstacle.x
        
        # Actualizar la posición
        self.obstacle.update()
        
        # Verificar que la posición X ha disminuido según la velocidad del juego
        self.assertEqual(self.obstacle.x, initial_x - self.game_speed)
    
    def test_obstacle_is_offscreen(self):
        """Test que verifica que el obstáculo detecta cuando está fuera de la pantalla."""
        # Inicialmente el obstáculo no está fuera de la pantalla
        self.assertFalse(self.obstacle.is_offscreen())
        
        # Mover el obstáculo fuera de la pantalla
        self.obstacle.x = -100
        self.obstacle.rect.midbottom = (self.obstacle.x, self.obstacle.y)
        
        # Verificar que ahora está fuera de la pantalla
        self.assertTrue(self.obstacle.is_offscreen())
    
    def test_obstacle_collision_rect(self):
        """Test que verifica que el rectángulo de colisión se actualiza correctamente."""
        initial_rect_pos = self.obstacle.rect.midbottom
        
        # Actualizar la posición
        self.obstacle.update()
        
        # Verificar que la posición del rectángulo ha cambiado
        self.assertNotEqual(self.obstacle.rect.midbottom, initial_rect_pos)
        self.assertEqual(self.obstacle.rect.midbottom, (self.obstacle.x, self.obstacle.y))

if __name__ == '__main__':
    unittest.main()