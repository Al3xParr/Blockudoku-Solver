import numpy as np

from shapes import Shape



class Board:
    
    def __init__(self) -> None:
        self.data = np.zeros((9, 9))



    def placeShape(self, shape: np.ndarray, location) -> bool:

        if shape.shape[0] + location[0] >= 9 or shape.shape[1] + location[1] >= 9:
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
            return True
        
    def showBoard(self):
        print(self.data)




b = Board()

b.placeShape(np.array(Shape.SQUARE.value), (1, 1))
b.placeShape(np.array(Shape.DIAG_THREE.value), (2, 2))
b.showBoard()