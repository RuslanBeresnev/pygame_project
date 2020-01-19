import ctypes

WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
FPS = 60

TILE_HEIGHT = 50
TILE_WIDTH = 50
