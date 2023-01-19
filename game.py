import pygame

from settings import *

from player import Player
from grid import Grid

class Game:
	def __init__(self):
		self.player_1 = Player('player_1', 'X', (255, 0, 0))
		self.player_2 = Player('player_2', 'O', (0, 0, 255))

		self.player_turn = self.player_1

		self.win_state = False
		self.win_alignement = []

		self.ancien_click_always_pressed = False

		self.grid = Grid(3)

		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(None, 50)

	def run(self):
		if not self.win_state:
			self.turn(self.player_turn)
			self.update_color_case()
		else:
			self.in_win_state()

		self.draw()

	def reset(self):
		self.grid = Grid(3)
		
		if self.player_turn.player_name == 'player_1':
			self.player_turn = self.player_2
			return

		elif self.player_turn.player_name == 'player_2':
			self.player_turn = self.player_1
			return

	def turn(self, player:Player):
		for col in self.grid.grid:
			for case in col:
				if case.hitbox.collidepoint(pygame.mouse.get_pos()) and case.actual_value == "" and pygame.mouse.get_pressed()[0] and not self.ancien_click_always_pressed:
					case.switch_value(player.player_sign)
					self.ancien_click_always_pressed = True

					if self.grid.alignement()[0]:
						self.win_state, self.win_alignement = self.grid.alignement()
						self.player_turn.player_score += 1
						self.player_turn.save_score()
						return

					if self.grid.all_case_have_value():
						self.win_state = True
						return

					if player.player_name == 'player_1':
						self.player_turn = self.player_2
						return

					elif player.player_name == 'player_2':
						self.player_turn = self.player_1
						return

				elif not pygame.mouse.get_pressed()[0]:
					self.ancien_click_always_pressed = False

	def in_win_state(self):
		for case in self.win_alignement:
			case.change_background_color(self.player_turn.color)

		if pygame.mouse.get_pressed()[0] and not self.ancien_click_always_pressed:
			self.reset()
			self.win_state = False
			self.ancien_click_always_pressed = True

		elif not pygame.mouse.get_pressed()[0]:
			self.ancien_click_always_pressed = False


	def update_color_case(self):
		for col in self.grid.grid:
			for case in col:
				if case.hitbox.collidepoint(pygame.mouse.get_pos()) and case.actual_value == "":
					case.change_background_color((125, 125, 125))
				else:
					case.change_background_color((255, 255, 255))

	def draw(self):
		for col in self.grid.grid:
			for case in col:
				self.display_surface.blit(case.image, case.hitbox.topleft)

		separated_lign_each_pixel = self.grid.pixel_size / 3
		width_center_corrector = (WIDTH - self.grid.pixel_size) / 2
		height_center_corrector = (HEIGHT - self.grid.pixel_size) / 2

		for i in range(1, self.grid.size):
			pygame.draw.rect(self.display_surface, (0, 0, 0), pygame.Rect( (width_center_corrector + separated_lign_each_pixel*i - GRID_WEIGHT/2, height_center_corrector), (GRID_WEIGHT, self.grid.pixel_size) ))

		for i in range(1, self.grid.size):
			pygame.draw.rect(self.display_surface, (0, 0, 0), pygame.Rect( (width_center_corrector, height_center_corrector + separated_lign_each_pixel*i - GRID_WEIGHT/2), (self.grid.pixel_size, GRID_WEIGHT) ))

		player_1_txt = self.font.render(f'player 1 : {self.player_1.player_score}', True, self.player_1.color)
		player_2_txt = self.font.render(f'player 2 : {self.player_2.player_score}', True, self.player_2.color)

		player_1_rect = player_1_txt.get_rect(topleft = (0,0))
		player_2_rect = player_2_txt.get_rect(topright = (WIDTH,0))

		self.display_surface.blit(player_1_txt, player_1_rect)
		self.display_surface.blit(player_2_txt, player_2_rect)

		if self.player_turn.player_name == self.player_1.player_name:
			rect = player_1_rect
			rect_color = self.player_1.color
		else:
			rect = player_2_rect
			rect_color = self.player_2.color

		rect.topleft = (rect.bottomleft[0], rect.bottomleft[1] + TEXT_UNDERLINE_MARGE)
		rect.height = TEXT_UNDERLINE_WEIGHT

		pygame.draw.rect(self.display_surface, rect_color, rect)

