from board import Board
import copy

def moveAI(board, player2):

	bestScore = -200000000000000 

	for i in range(9):

		if board.legalMove(i + 1):
			board_copy= copy.deepcopy(board)
			board_copy.move(i + 1, player2)
			score = minimax(board_copy, 0, -200000000000000, +200000000000000, False, player2)

			if score > bestScore:
				bestScore = score
				bestMove  = i + 1

	return bestMove			

def minimax(board, depth, alpha, beta, maximisingPlayer, player2):

	scores = gameScores(player2)

	if board.finished():
		return scores[board.winner]

	if maximisingPlayer:
		eval = -200000000000000

		for i in range(9):

			if board.legalMove(i + 1):
				board_copy = copy.deepcopy(board)
				board_copy.move(i + 1, player2)
				eval = max(eval, minimax(board_copy, depth + 1, alpha, beta, False, player2))
				alpha = max(alpha, eval)
				if (alpha >= beta):
					break
		return eval
	else:
		eval = +200000000000000

		for i in range(9):

			if board.legalMove(i + 1):
				board_copy = copy.deepcopy(board)
				player1 = otherPlayer(player2)
				board_copy.move(i + 1, player1)
				eval = min(eval ,minimax(board_copy, depth + 1, alpha, beta, True, player2))
				beta = min(beta, eval)
				if (beta <= alpha):
					break
		return eval


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
