import pygame

from settings import *


class Case:
	def __init__(self, all_image:dict, possible_mutation_number:int, pos_x:int, pos_y:int,img_size:int = 150):
		if len(all_image) == 0:
			raise ValueError('possible_value need to have more than 0 value.')

		self.hitbox = pygame.Rect( (pos_x, pos_y), (img_size, img_size) )

		self.actual_value = ""

		self.all_image = all_image
		for key in all_image:
			self.all_image[key] = pygame.transform.scale(self.all_image[key], (img_size, img_size))

		self.all_image[""] = pygame.surface.Surface((img_size, img_size)).convert_alpha()
		self.all_image[""].fill((0, 0, 0, 0))

		self.possible_mutation_number = possible_mutation_number

		self.background = pygame.surface.Surface((img_size, img_size))
		self.background.fill(BACKGROUND)

	def switch_value(self, value):
		if value not in self.all_image.keys():
			raise ValueError('switch value not in possible value.')

		if self.possible_mutation_number == 0:
			return

		self.possible_mutation_number -= 1
		self.actual_value = value

	def change_background_color(self, new_color:tuple):
		try:
			self.background.fill(new_color)
		except:
			raise ValueError('new_color is not code has a color.')

	@property
	def image(self):
		img = self.background.copy()
		img.blit(self.all_image[self.actual_value], (0, 0))
		return img

	def __str__(self):
		return self.actual_value
