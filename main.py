# basic module #
import sys

# free module #
import pygame

# my module #
from settings import *

from game import *

class Window():
	def __init__(self):
		pygame.init()

		pygame.mouse.set_visible(True)

		pygame.display.set_caption("morpion")
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.game = Game()

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.screen.fill(BACKGROUND)

			self.game.run()

			pygame.display.update()


		pygame.quit()

if __name__ == '__main__':
	window = Window()
	window.run()