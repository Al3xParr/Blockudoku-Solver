import numpy as np
from shapes import Shape
from board import Board


class Player:
    def __init__(self) -> None:
        pass
    
    
    def playMove(self, board: np.ndarray, shape: Shape) -> bool:
        pass
    

    def decideMove(self, board: Board, shapes: list) -> tuple:
        pass
