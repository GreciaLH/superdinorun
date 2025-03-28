# Configuración del Juego
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
GROUND_HEIGHT = SCREEN_HEIGHT - 60
FPS = 60

# Velocidades y física
INITIAL_GAME_SPEED = 6.0
SPEED_INCREASE_FACTOR = 0.001
GRAVITY = 0.7
JUMP_FORCE = -15
SPAWN_RATE = 90
MIN_SPAWN_RATE = 45

# Colores (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
GROUND_BROWN = (210, 180, 140)
DINO_GREEN = (80, 180, 80)
CACTUS_GREEN = (0, 150, 0)
MOUNTAIN_DARK = (100, 100, 120)
MOUNTAIN_LIGHT = (140, 140, 160)
CLOUD_COLOR = (240, 240, 240, 200)
TEXT_COLOR = (0, 0, 0)
GAMEOVER_OVERLAY = (180, 0, 0, 180)
START_OVERLAY = (0, 0, 0, 150)

# Datos de sprites
DINO_SPRITE_DATA = {
    'color': DINO_GREEN,
    'body': ((-15, -30), (30, 30)),  # (x, y), (w, h) relativo al centro
    'head': ((5, -50), (20, 20)),
    'tail': ((-35, -25), (20, 10)),
    'leg1': ((-10, 0), (8, 15)),
    'leg2': ((2, 0), (8, 15)),
    'eye': ((15, -43), (4, 4)),
    'eye_color': BLACK,
    'width': 50,
    'height': 55
}

CACTUS_SPRITE_DATA = {
    'color': CACTUS_GREEN,
    'base': ((0, -20), (15, 40)),  # (x, y), (w, h) relativo al centro inferior
    'arm1': ((-12, -25), (10, 20)),
    'arm2': ((12, -30), (10, 25)),
    'width': 30,
    'height': 50
}

CLOUD_SPRITE_DATA = {
    'color': CLOUD_COLOR,
    'parts': [
        {'x': -20, 'y': -10, 'w': 30, 'h': 20},
        {'x': 0, 'y': -15, 'w': 40, 'h': 25},
        {'x': 25, 'y': -8, 'w': 25, 'h': 18}
    ]
}

MOUNTAIN_SPRITE_DATA = {
    'color1': MOUNTAIN_DARK,
    'color2': MOUNTAIN_LIGHT,
    'base_width': 200,
    'height': 150
}