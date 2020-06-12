from board import Board
from minimax import moveAI

class Game:

	def __init__(self):
		
		self.board = Board()

		self.player1 = input("Do you want to play as X or 0? ")
		self.player2 = self.otherPlayer(self.player1)

		startDecision = input("Do you want to start? (y/n): ")
		self.turn = self.whoStarts(self.player1, startDecision)

	def otherPlayer(self, player1):

		if player1 == "X":
			return "O"
		else:
			return "X"

	def whoStarts(self, player1, startDecision):

		if startDecision == "y":
			return self.player1
		else:
			return self.otherPlayer(self.player1)

	def play(self):

		while not self.board.finished():

			self.board.display()
			if self.turn == self.player1:
				position = int(input("Where do you want to play? "))

				if self.board.legalMove(position):
					self.board.move(position, self.turn)
					self.turn = self.otherPlayer(self.turn)
				else:
					print("Please play a legal move ")
			else:
				print("Computer plays ")
				move = moveAI(self.board, self.player2)
				self.board.move(move, self.turn)
				self.turn = self.otherPlayer(self.turn)	

		# Finishing Screen
		self.board.display()
		if self.board.winner == "tie":
			print("Its a tie!")	
		else:
			print(f"Player {self.board.winner} wins!")