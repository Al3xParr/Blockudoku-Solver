from enum import Enum
import numpy as np
import random




class Shape(Enum):
    FIVE = [[1, 1, 1, 1, 1]]
    FOUR = [[1, 1, 1, 1]]
    THREE = [[1, 1, 1]]
    TWO = [[1, 1]]
    ONE = [[1]]
    SQUARE = [[1, 1], [1, 1]]
    CROSS = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    STEP = [[1, 0], [1, 1]]
    LARGE_STEP = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
    DIAG_THREE = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    DIAG_TWO = [[1, 0], [0, 1]]
    L = [[1, 0, 0], [1, 1, 1]]
    RIGHT_ANGLE = [[1, 0, 0], [1, 0, 0], [1, 1, 1]]
    T = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
    SHORT_T = [[1, 1, 1], [0, 1, 0]]
    
    def getValue(self):
        return np.array(self.value, dtype="int8")


def getRandomShape() -> np.ndarray:
    choice = random.choice([x for x in Shape])

    rtn = choice.getValue()
    
    return np.rot90(rtn, k=random.randint(0, 3))


def printShape(shape: np.ndarray) -> None:
    for row in shape:
        rowString = np.array2string(row)
        rowString = rowString.replace("[", "").replace("]", "")
        rowString = rowString.replace("1", "\u220e").replace("0", "_")
        print(rowString)
    