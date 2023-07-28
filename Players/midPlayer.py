from .players import Player
from board import Board
from shapes import Move
import numpy as np
import math

# This example of a player will paly the move given the sahpe options 
# and board that will give the immediate best score after that one move.
# If multiple 
class MidPlayerLow(Player):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "MidLow"

    
    def decideMove(self, board: Board, shapes: list, silent: bool = False) -> tuple:
        bestMove = None
        bestMoveScore = 0
        bestShape = None
        bestBoardRating = 0
        bestPlacementRating = 0

        for i, shape in enumerate(shapes):
            for col in range(9):
                for row in range(9):
                    boardAfterMove, score = board.evaluateMove(shape, (row, col))
                    
                    if score is not None:
                        
                        boardRating = self.evaluateBoardState(boardAfterMove)
                        
                        placementRating = self.evaluatePlacement(shape, row, col)
                        
                        newBest = score > bestMoveScore                          
                        
                        newBest = newBest or (score == bestMoveScore and boardRating < bestBoardRating)
                        #newBest = newBest or (score == bestMoveScore and placementRating < bestPlacementRating)
                        
                        if newBest:
                            bestMove = (row, col)
                            bestMoveScore = score
                            bestBoardRating = boardRating
                            bestShape = i
                            
                    
        if bestMove is None:
            if not silent: print("no available moves")
            return None, None
        
        self.movesPlayed.append(Move(shapes[bestShape], bestMove))
              
        return bestShape, bestMove

    # Returns a number representing the quality of each deletable section combined
    def evaluateBoardState(self, board: Board) -> int:
        overallRating = 0
        
        for colIdx in range(board.shape[1]):
            sec = board[:, colIdx].reshape(9)
            overallRating += self.rateSection(sec)
                
        # Check rows
        for rowIdx in range(board.shape[0]):
            sec = board[rowIdx, :].reshape(9)
            overallRating += self.rateSection(sec)

        # Check squares
        for i in range(9):
            x = 3 * math.floor(i/3)
            y =  3 * (i % 3)
            
            sec = board[x : x + 3, y : y + 3].reshape(9)
            overallRating += self.rateSection(sec)
        
        #Returns the rating normalised to the max value it could be (108)
        return overallRating/108
            
    # Returns a number representing the quality of a section based on how many free tiles there are
    # 0 -> 0; 1 -> 1; 2 -> 2; 3 -> 3; 4 -> 4; 5 -> 4; 6 -> 3; 7 -> 2; 8 -> 1
    # Lower is better
    def rateSection(self, section: np.ndarray) -> int:
        if np.all(section == 0): return 0
        rating = np.count_nonzero(section == 1)

        return rating if rating < 4 else 9 - rating
    
    def getNumSqr(self, row, col) -> int:
        return math.floor(col/3) + 3 * math.floor(row/3)
    
    # Return the number of mini squares the shape being placed in a given
    # location will occupy. Lower is better
    def evaluatePlacement(self, shape: np.ndarray, row, col) -> int:
        populatedSquares = set()
        
        for r in range(shape.shape[0]):
            for c in range(shape.shape[1]):
                if shape[r, c] == 1:
                    populatedSquares.add(self.getNumSqr(row + r, col + c))
                    
        return len(populatedSquares)

class MidPlayerHigh(MidPlayerLow):
    def __init__(self) -> None:
        super().__init__()
        self.name = "MidHigh"
    
    def evaluateBoardState(self, board: Board) -> int:
        openAreasRating = self.evaluateAreas(board)
        superRating = super().evaluateBoardState(board)

        return openAreasRating / 2 + superRating
    
    def pointAdjacent(self, point, pointList) -> bool:
        for p in pointList:
            #print(point, p)
            dist = math.sqrt((point[0] - p[0]) ** 2 + (point[1] - p[1]) ** 2)
            #print(dist)
            if dist == 1:
                return True
        
        return False
        
            
    def evaluateAreas(self, board: Board) -> int:

        indexes = np.vstack(np.where(board == 0))


        emptyAreas = []
        
        for idx in indexes.T:

            for i, area in enumerate(emptyAreas):
                
                if self.pointAdjacent(idx, area):
                    emptyAreas[i].append(idx)
                    break
                    
                if i + 1 == len(emptyAreas):

                    emptyAreas.append([idx])
                    break
                    
            if len(emptyAreas) == 0:
                emptyAreas.append([idx])


        eval = [len(x)**2 for x in emptyAreas]
        

        return 1 - (sum(eval)/8561)
        
        