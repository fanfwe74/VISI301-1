import pygame
import math
from gl0bals import *

class Projectile():

	def __init__(self, x, y, x_aim, y_aim):

		self.x = x # x initial
		self.y = y # y initial
		self.width = 0.5 * Globals.RATIO
		self.rect = pygame.Rect((self.x, self.y), (self.width,self.width)) # hitbox
		self.x_aim = x_aim # x visé
		self.y_aim = y_aim # y visé
		self.vx_direct = self.x_aim - self.x
		self.vy_direct = self.y_aim - self.y
		self.dist = math.sqrt((self.vx_direct)**2 + (self.vy_direct)**2)
		self.v_fixed = 0.2 * Globals.RATIO
		self.coef = self.dist / self.v_fixed
		self.vx = self.vx_direct / self.coef
		self.vy = self.vy_direct / self.coef

		self.sprites = [pygame.image.load("./ressources/projectile/1.png").convert_alpha(),
						pygame.image.load("./ressources/projectile/2.png").convert_alpha()]
		self.animation_counter = 0
		self.sprite = self.sprites [self.animation_counter]

		Globals.projectiles.append(self)


	def move_single_axis(self):
		self.rect.x += self.vx
		self.rect.y += self.vy

		# correction de bug de manière brutale
		if self.rect.y == 0 and -1 < self.vy <= 0:
			self.rect.y = -100


	def animation(self):
		"""Oriente le sprite joueur selon son dernier mouvement"""

		# passe au sprite suivant toute les 10 images (0.2 sec)
		if Globals.counter%10 == 0:
			self.animation_counter += 1
		# revient au premier sprite une fois le 2e sprite passé
		if self.animation_counter >= len(self.sprites):
			self.animation_counter = 0

		self.sprite = self.sprites[self.animation_counter]