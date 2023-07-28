import numpy as np
import math
from shapes import Shape
import copy


class Board:
    
    def __init__(self) -> None:
        self.data = np.zeros((9, 9), dtype="int8")
        self.score = 0
        self.moves = 0
    
    def getBoard(self) -> np.ndarray:
        return self.data
    
    # Evaluates the outcome of a move, returning a tuple of (board after move, score increment)
    def evaluateMove(self, shape: np.ndarray, location) -> tuple:
        
        if shape.shape[0] + location[0] > 9 or shape.shape[1] + location[1] > 9:
            return None, None
        
        xBefore = location[0]
        xAfter = 9 - shape.shape[0] - xBefore
        yBefore = location[1]
        yAfter = 9 - shape.shape[1] - yBefore
        paddedShape = np.pad(shape, ((xBefore, xAfter),(yBefore, yAfter)), mode='constant')
        
        boardAndShape = np.copy(self.data) + paddedShape
        
        # Checks if the move is invalid
        if np.any(boardAndShape == 2):
            return None, None
        
        boardAfterScoring, scoreInc, multiplier = self.verify(boardAndShape)
        scoreInc += np.count_nonzero(shape)
        scoreInc *= multiplier
        
        return boardAfterScoring, scoreInc



    def placeShape(self, shape: np.ndarray, location) -> bool:
        
        newBoard, scoreInc = self.evaluateMove(shape, location)
        
        if newBoard is None or scoreInc is None:
            return False

        self.data = newBoard
        self.score += scoreInc
        self.moves += 1
        return True

    
    
    # Function to assess any complete lines and squares that are to be removed and score incremented.
    # If real is True, score and new board is applied to the class
    def verify(self, customBoard: np.ndarray = None) -> tuple:
        combos = 0
        scoreInc = 0
        multiplier = 1
        
        if customBoard is None:
            inpBoard = np.copy(self.data)
        else:
            inpBoard = customBoard
        newBoard = copy.deepcopy(inpBoard)
        
        # Check cols
        for colIdx in range(inpBoard.shape[1]):
            col = inpBoard[:, colIdx]
            if np.all(col == 1):
                scoreInc += 18
                newBoard[:, colIdx] = 0
                combos += 1
                
        # Check rows
        for rowIdx in range(inpBoard.shape[0]):
            row = inpBoard[rowIdx, :]
            if np.all(row == 1):
                scoreInc += 18
                newBoard[rowIdx, :] = 0
                combos += 1
                   
        # Check squares
        for i in range(9):
            x = 3 * math.floor(i/3)
            y =  3 * (i % 3)
            
            sqr = inpBoard[x : x + 3, y : y + 3]
            if np.all(sqr == 1):
                scoreInc += 18
                newBoard[x : x + 3, y : y + 3] = 0    
                combos += 1    
        
        match combos:
            case 0:
                multiplier = 1
            case 1:
                multiplier = 1
            case 2:
                multiplier = 2
            case 3:
                multiplier = 3
            case 4:
                multiplier = 5
            case _:
                multiplier = 10
        
        return newBoard, scoreInc, multiplier

    def showBoard(self):
        for row in self.data:
            rowString = np.array2string(row)
            rowString = rowString.replace("[", "").replace("]", "")
            rowString = rowString.replace("1", "\u220e").replace("0", "_")
            
            print(rowString)
        
        