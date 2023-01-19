import pygame

from .case import Case
from settings import *

class Grid:
	def __init__(self, size:int):
		if size <= 2:
			raise ValueError('size can\'t be under 3')

		all_images = {
			'X': pygame.image.load(f'{PATH}/img/croix.png'),
			'O': pygame.image.load(f'{PATH}/img/rond.png'),
			}

		self.size = size
		self.pixel_size = CASE_SIZE * size + CASE_SPACE_AROUND * (size - 1)

		width_center_corrector = (WIDTH - self.pixel_size) / 2
		height_center_corrector = (HEIGHT - self.pixel_size) / 2

		self.grid = [ [Case( all_images, 1, x * (CASE_SIZE + CASE_SPACE_AROUND) + width_center_corrector, y * (CASE_SIZE + CASE_SPACE_AROUND) + height_center_corrector,CASE_SIZE) for y in range(0, size)] for x in range(0, size)]

	def get(self, col:int, index:int):
		try:
			return self.grid[col][index]
		except:
			return None

	def change(self, col:int, index:int, new_val:str):
		self.grid[col][index].switch_value(new_val)

	def hori_have_same_value(self):
		for col in self.grid:
			verif = col[0].actual_value
			res = True
			for i in col:
				if verif != i.actual_value or i.actual_value == "":
				 	res = False
				 	break
			if res == True:
				return True, col

		return False, None

	def vert_have_same_value(self):
		for i in range(0, self.size):
			verif = self.grid[0][i].actual_value
			res = True
			for col in self.grid:
				if verif != col[i].actual_value or col[i].actual_value == "":
					res = False
					break

			if res == True:
				return True, [col[i] for col in self.grid]

		return False, None

	def diag_have_same_value(self):
		val_in_left_diago = []
		case_in_left_diago = []

		val_in_right_diago = []
		case_in_right_diago = []

		for n, l in zip(range(self.size), self.grid):
			val_in_left_diago.append(l[n].actual_value)
			case_in_left_diago.append(l[n])

			val_in_right_diago.append(l[ -(n+1) ].actual_value)
			case_in_right_diago.append(l[ -(n+1) ])

		left_verif = val_in_left_diago[0]
		left_res = True
		for val in val_in_left_diago:
			if left_verif != val or left_verif == "":
				left_res = False
				break

		if left_res == True:
			return True, case_in_left_diago

		right_verif = val_in_right_diago[0]
		for val in val_in_right_diago:
			if right_verif != val or right_verif == "":
				return False, None

		return True, case_in_right_diago

	def alignement(self):
		if self.hori_have_same_value()[0]:
			return self.hori_have_same_value()

		if self.vert_have_same_value()[0]:
			return self.vert_have_same_value()

		if self.diag_have_same_value()[0]:
			return self.diag_have_same_value()

		return False, None

	def all_case_have_value(self):
		for col in self.grid:
			for case in col:
				if case.actual_value == "":
					return False

		return True

	def __str__(self):
		txt = ""
		for col in self.grid:
			for val in col:
				txt += val.actual_value + "	"

			txt += "\n"
		return txt