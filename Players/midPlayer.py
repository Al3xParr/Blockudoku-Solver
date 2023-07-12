from .players import Player
from board import Board
from shapes import Move
import numpy as np
import math

# This example of a player will paly the move given the sahpe options 
# and board that will give the immediate best score after that one move.
# If multiple 
class MidPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()

    
    def decideMove(self, board: Board, shapes: list, silent: bool = False) -> tuple:
        bestMove = None
        bestMoveScore = 0
        bestShape = None
        bestBoardRating = 0
        
        
        for i in range(len(shapes)):
            for col in range(9):
                for row in range(9):
                    boardAfterMove, score = board.evaluateMove(shapes[i], (row, col))
                    
                    if score is not None:
                        
                        boardRating = self.evaluateBoardState(boardAfterMove)
                        
                        if score > bestMoveScore:
                            bestMove = (row, col)
                            bestMoveScore = score
                            bestShape = i
                        elif score == bestMoveScore and boardRating > bestBoardRating:
                            bestMove = (row, col)
                            bestMoveScore = score
                            bestShape = i
                    
        if bestMove is None:
            if not silent: print("no available moves")
            return None, None
        
        self.movesPlayed.append(Move(shapes[bestShape], bestMove))
              
        return bestShape, bestMove

    
    def evaluateBoardState(self, board: Board) -> int:
        overallRating = 0
        
        for colIdx in range(board.shape[1]):
            sec = board[:, colIdx].reshape(9)
            overallRating += self.rateSection(sec)
                
        # Check rows
        for rowIdx in range(board.shape[0]):
            sec = board[rowIdx, :].reshape(9)
            overallRating += self.rateSection(sec)

        # Check squares
        for i in range(9):
            x = 3 * math.floor(i/3)
            y =  3 * (i % 3)
            
            sec = board[x : x + 3, y : y + 3].reshape(9)
            overallRating += self.rateSection(sec)
        
        return overallRating
            
                            
    def rateSection(self, section: np.ndarray) -> int:
        if np.all(section == 0): return 0
        rating = np.count_nonzero(section == 1)

        return rating if rating < 4 else 9 - rating
