from board import Board
import copy

def moveAI(board, player2):

	bestScore = -200000000000000 

	for i in range(9):

		if board.legalMove(i + 1):
			board_copy= copy.deepcopy(board)
			board_copy.move(i + 1, player2)
			score = minimax(board_copy, 0, False, player2)

			if score > bestScore:
				bestScore = score
				bestMove  = i + 1

	return bestMove			

def minimax(board, depth, maximisingPlayer, player2):

	scores = gameScores(player2)

	if board.finished():
		return scores[board.winner]

	if maximisingPlayer:
		maxEval = -200000000000000

		for i in range(9):

			if board.legalMove(i + 1):
				board_copy = copy.deepcopy(board)
				board_copy.move(i + 1, player2)
				eval = minimax(board_copy, depth + 1, False, player2)
				maxEval = max(maxEval, eval)

		return maxEval
	else:
		minEval = +200000000000000

		for i in range(9):

			if board.legalMove(i + 1):
				board_copy = copy.deepcopy(board)
				player1 = otherPlayer(player2)
				board_copy.move(i + 1, player1)
				eval = minimax(board_copy, depth + 1, True, player2)
				minEval = min(minEval, eval)

		return minEval


# Helper functions
def gameScores(player2):

	if player2 == "O":
		return { "O": 1, "tie": 0, "X": -1}
	else:
		return { "X": 1, "tie": 0, "O": -1}

def otherPlayer(player):

	if player == "X":
		return "O"
	else:
		return "X"
