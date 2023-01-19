from settings import *

class Player:
	def __init__(self, player_name:str, player_sign:str, color:tuple):
		self.player_name = player_name
		self.player_score = 0

		self.player_sign = player_sign
		self.color = color

		with open(SCORE_PATH) as score_file:
			for line in score_file.readlines():
				if player_name in line.split(':'):
					try:
						self.player_score = int(line.split(':')[1])
						break
					except:
						break

	def save_score(self):
		score_found = False

		with open(SCORE_PATH, 'r+') as score_file:
			file_content = score_file.readlines()
			for line, index in zip( file_content, range( len(file_content) ) ):
				if self.player_name in line.split(':'):
					file_content[index] = f'{self.player_name}:{self.player_score}\n'
					score_found = True
			score_file.seek(0)
			score_file.truncate()

			for line in file_content:
				score_file.write(f'{line}')

		if not score_found:
			with open(SCORE_PATH, 'a') as score_file:
				score_file.write(f'{self.player_name}:{self.player_score}')