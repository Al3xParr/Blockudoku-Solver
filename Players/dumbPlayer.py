from .players import Player
from board import Board

class DumbPlayer(Player):
    
    def __init__(self) -> None:
        pass
    
    def decideMove(self, board: Board, shapes: list) -> tuple:
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
            print("no available moves")
            return None, None
              
        return bestShape, bestMove
                            
        