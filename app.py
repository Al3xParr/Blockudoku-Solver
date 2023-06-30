from board import Board
from shapes import Shape, getRandomShape
from Players.dumbPlayer import DumbPlayer
import numpy as np

def startGame():
    # Initialise everything
    board = Board()
    aiPlayer = DumbPlayer()
    continuePlay = True
    moveCount = 0

    for i in range(10):
        shapeOptions = [getRandomShape() for j in range(3)]

        while len(shapeOptions) > 0: 
            choiceIdx, location = aiPlayer.decideMove(board, shapeOptions)
            
            if choiceIdx == None and location == None:
                continuePlay = False
                endGame(board)
            
            board.placeShape(shapeOptions[choiceIdx], location)
            
            print("Move made; score: {}".format(board.score))
            
            shapeOptions.pop(choiceIdx)
            print(shapeOptions)

            moveCount += 1

            #if moveCount % 10 == 0:
            board.showBoard()
            
    board.showBoard()
   
def endGame(board: Board):
    print(board.showBoard())
    print("Score: {}".format(board.score))
    
if __name__ == "__main__":
    startGame()