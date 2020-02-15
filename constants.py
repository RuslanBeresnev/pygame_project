import ctypes
import pygame

WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)