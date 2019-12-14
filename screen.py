import pygame
from globals import *

class Screen():

	def __init__(self):

		self.resolution = (1280,720)
		self.surface = pygame.display.set_mode((self.resolution))
		self.fullscreen = False
		self.icon = pygame.image.load("ressources/icon.jpg")
		pygame.display.set_icon(self.icon) # icône de la fenêtre
		pygame.display.set_caption("Goodoo") # titre de la fenêtre