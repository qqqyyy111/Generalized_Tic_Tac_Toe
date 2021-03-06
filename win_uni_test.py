# @Author Zhihan Jiang
import math
import numpy as np

# class to represent a game
class Game:

	# scale parameters and board initializer
	def __init__(self, scale, combo):
		self.scale = scale
		self.combo = combo
		self.board = []
		self.winner = ''
		
		# uni-dimentional representation
		while len(self.board) < math.pow(self.scale, 2):
			self.board.append(" ")

		
		self.board[3] = "B"
		self.board[4] = "B"
		self.board[5] = "B"

		self.board[7] = "W"
		self.board[11] = "W"
		self.board[13] = "W"
		self.board[14] = "W"
		self.board[15] = "W"
		self.board[23] = "B"
		self.board[31] = "W"

		self.board[21] = "W"
		self.board[28] = "W"

		
		self.reshape()

		print(f'New game created with a scale of {scale} and a combo of {combo}.')

	# function to reshape and produce a convenient representation
	def reshape(self):
		data = np.array(self.board)
		shape = (self.scale, self.scale)
		self.shaped = data.reshape(shape)

	# function to display the board of the game
	def print_board(self):
		print(self.shaped)
	
	# function to place a stone at a given positioon
	def place_stone(location, player):
		self.board[location] = player
		self.reshape()

	# function to perform generalized row check
	def check_general_rows(self, rows, player):
		current_player = " "
		for row in rows:
				for index, place in enumerate(row):
					check_space = []
					
					begin = 0
					while len(check_space) < self.combo:
						# if self.has_right(index + begin):
						if index + begin <= len(row) - 1:
							if row[index + begin] == player:
								check_space.append(row[index + begin])
								begin = begin + 1
							else:
								break
						else:
							break

					if len(check_space) == self.combo:
						current_player = player
						print(f'{player} win!')
						return current_player
		return current_player


	# function to see if we have a winner
	def check_win(self):
		
		for player in ["B", "W"]:

			# check horizontal
			current_player1 = self.check_general_rows(self.shaped, player)
			if current_player1 == 'B':
                return "B"
            elif current_player1 == 'W':
                return "W"

			# check vertical
			rotated = zip(*self.shaped[::-1])
			current_player2 = self.check_general_rows(rotated, player)
            if current_player2 == 'B':
                return "B"
            elif current_player2 == 'W':
                return "W"

			# check diagonal
			diags = [self.shaped[::-1,:].diagonal(i) for i in range(-self.shaped.shape[0]+1,self.shaped.shape[1])]
			diags.extend(self.shaped.diagonal(i) for i in range(self.shaped.shape[1]-1,-self.shaped.shape[0],-1))
			 current_player3 = self.check_general_rows(diags, player)

            if current_player3 == 'B':
                return "B"
            elif current_player3 == 'W':
                return "W"

		if self.winner is '':
			print('winner unknown yet')


# unit test part below:
if __name__ == '__main__':
	newgame = Game(8, 4)
	newgame.print_board()

	newgame.check_win()