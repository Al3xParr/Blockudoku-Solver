from .players import Player
from board import Board

class DumbPlayer(Player):
    
    def __init__(self) -> None:
        pass
    
    def decideMove(self, board: Board, shapes: list) -> tuple:
        bestMove = None
        bestMoveScore = None
        
        for col in range(9):
            for row in range(9):
                _, score = board.evaluateMove(shapes[0], (row, col))
                if score is not None:
                    if score > 0 if bestMoveScore is None else bestMoveScore:
                        bestMove = (row, col)
                        bestMoveScore = score
                    
        if bestMove is None:
            print("no available moves")
            return None, None
              
        
        return 0, bestMove        
                            
        