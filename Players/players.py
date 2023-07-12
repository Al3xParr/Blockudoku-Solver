import numpy as np
from shapes import Shape
from board import Board


class Player:
    def __init__(self) -> None:
        self.movesPlayed = []
    

    def decideMove(self, board: Board, shapes: list, silent: bool = False) -> tuple:
        pass
