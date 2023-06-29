import numpy as np
from shapes import Shape


class Player:
    def __init__(self) -> None:
        pass
    
    
    def playMove(self, board: np.ndarray, shape: Shape) -> bool:
        pass
    
    
    def checkMove(self, board: np.ndarray, shape: Shape, location: tuple) -> bool:
        shape = np.array(shape.value)
        if shape.shape[0] + location[0] >= 9 or shape.shape[1] + location[1] >= 9:
            return False
        
        xBefore = location[0]
        xAfter = 9 - shape.shape[0] - xBefore
        yBefore = location[1]
        yAfter = 9 - shape.shape[1] - yBefore
        
        paddedShape = np.pad(shape, ((xBefore, xAfter),(yBefore, yAfter)), mode='constant')

        tempBoard = np.copy(board)
        tempBoard += paddedShape
        
        if np.any(tempBoard == 2):
            return False
        else:
            return True
        