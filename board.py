class Board:
	
	def __init__(self):
		
		self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
		self.winner = None

	def display(self):

		table = f"""
		{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
		---------
		{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
		---------
		{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
		"""
		print(table)


	def legalMove(self, position):

		if position == 0 or position > 9:
			return False

		row    = int( (position - 1) / 3)
		column = (position - 1) % 3 
		if (self.board[row][column] == "O") or (self.board[row][column] == "X"):
			return False
		else:
			return True

	def move(self, position, player):

		row    = int( (position - 1) / 3)
		column = (position - 1) % 3 

		self.board[row][column] = player

	def finished(self):

		for i in range(3):

			# rows
			if (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]):
				self.winner = self.board[i][0]
				return True

			# colunms 
			if (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]):
				self.winner = self.board[0][i]
				return True


		# diagonals
		if (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
			self.winner = self.board[0][0]
			return True

		if (self.board[2][0] == self.board[1][1]) and (self.board[1][1] == self.board[0][2]):
			self.winner = self.board[2][0]
			return True

		# checking if it is a tie
		counter = 0
		for i in range(9):

			if not self.legalMove(i+1):
				counter += 1

		if counter == 9:
			self.winner = "tie"
			return True

		return False










