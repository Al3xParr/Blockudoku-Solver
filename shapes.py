from enum import Enum
import numpy as np


"""
class Shape(Enum):
    FIVE = np.array([1, 1, 1, 1, 1])
    FOUR = np.array([1, 1, 1, 1])
    THREE = np.array([1, 1, 1])
    TWO = np.array([1, 1])
    ONE = np.array([1])
    SQUARE = np.array([[1, 1], [1, 1]])
    CROSS = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    STEP = np.array([[1, 0], [1, 1]])
    LARGE_STEP = np.array([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
    DIAG_THREE = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    DIAG_TWO = np.array([[1, 0], [0, 1]])
    L = np.array([[1, 0, 0], [1, 1, 1]])
    RIGHT_ANGLE = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
    T = np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0]])
    SHORT_T = np.array([[1, 1, 1], [0, 1, 0]])
    """
    
    
class Shape(Enum):
    FIVE = [1, 1, 1, 1, 1]
    FOUR = [1, 1, 1, 1]
    THREE = [1, 1, 1]
    TWO = [1, 1]
    ONE = [1]
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

    