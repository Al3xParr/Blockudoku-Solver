import numpy as np
import math
from shapes import Shape



class Board:
    
    def __init__(self) -> None:
        self.data = np.zeros((9, 9))



    def placeShape(self, shape: np.ndarray, location) -> bool:

        #shapeSize = (shape.shape[0], 1 if len(shape.shape) == 1 else shape.shape[1])


        
        #Check if shape will be outside of board
        if shape.shape[0] + location[0] > 9 or shape.shape[1] + location[1] > 9:
            return False
        
        xBefore = location[0]
        xAfter = 9 - shape.shape[0] - xBefore
        yBefore = location[1]
        yAfter = 9 - shape.shape[1] - yBefore
        paddedShape = np.pad(shape, ((xBefore, xAfter),(yBefore, yAfter)), mode='constant')

        tempData = np.copy(self.data)
        tempData += paddedShape
        
        if np.any(tempData == 2):
            return False
        else:
            self.data = tempData
            self.verify()
            return True
    
    def verify(self) -> None:
        fullCols = []
        fullRows = []
        fullSqrs = []
        
        newBoard = np.copy(self.data)
        
        # Check cols
        for colIdx in range(self.data.shape[1]):
            col = self.data[:, colIdx]
            if np.all(col == 1):
                newBoard[:, colIdx] = 0
                
        # Check rows
        for rowIdx in range(self.data.shape[0]):
            row = self.data[rowIdx, :]
            if np.all(row == 1):
                newBoard[rowIdx, :] = 0
                   
        # Check squares
        for i in range(9):
            x = 3 * math.floor(i/3)
            y =  3 * (i % 3)
            
            sqr = self.data[x : x + 3, y : y + 3]
            if np.all(sqr == 1):
                newBoard[x : x + 3, y : y + 3] = 0        
            
        self.data = newBoard  
        
    def showBoard(self):
        print(self.data)


"""
b = Board()

b.placeShape(np.array(Shape.SQUARE.value), (1, 1))
b.placeShape(np.array(Shape.DIAG_THREE.value), (2, 2))
b.showBoard()
"""