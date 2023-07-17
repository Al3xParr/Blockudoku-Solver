from .players import Player
from board import Board
from shapes import Move

# This example of a player will paly the move given the sahpe options 
# and board that will give the immediate best score after that one move.
# If multiple 
class DumbPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "Dumb"

    
    def decideMove(self, board: Board, shapes: list, silent: bool = False) -> tuple:
        bestMove = None
        bestMoveScore = 0
        bestShape = None
        possibles = 0
        
        
        for i in range(len(shapes)):
            for col in range(9):
                for row in range(9):
                    _, score = board.evaluateMove(shapes[i], (row, col))
                    if score is not None:
                        if score > bestMoveScore:
                            possibles += 1
                            bestMove = (row, col)
                            bestMoveScore = score
                            bestShape = i
                    
        if bestMove is None:
            if not silent: print("no available moves")
            return None, None
        
        self.movesPlayed.append(Move(shapes[bestShape], bestMove))
              
        return bestShape, bestMove
                            
        