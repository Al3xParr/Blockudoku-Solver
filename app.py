from board import Board
from shapes import Shape
from Players.dumbPlayer import DumbPlayer
import numpy as np

def startGame():
    # Initialise everything
    board = Board()
    aiPlayer = DumbPlayer()
    again = True


    board.placeShape(np.array(Shape.SQUARE.value), (0, 0))
    board.placeShape(np.array(Shape.SQUARE.value), (0, 2))
    board.placeShape(np.array(Shape.SQUARE.value), (2, 0))
    board.placeShape(np.array(Shape.SQUARE.value), (2, 2))
    board.placeShape(np.array(Shape.ONE.value), (0, 8))
    board.showBoard()
    
    
    
    
if __name__ == "__main__":
    startGame()