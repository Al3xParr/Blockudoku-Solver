from board import Board
from shapes import Shape, getRandomShape
from Players.dumbPlayer import DumbPlayer
import numpy as np
import copy

def startGame():
    # Initialise everything
    board = Board()
    aiPlayer = DumbPlayer()
    continuePlay = True
    moveCount = 0

    while continuePlay:
        shapeOptions = [getRandomShape() for j in range(3)]

        while len(shapeOptions) > 0: 
            choiceIdx, location = aiPlayer.decideMove(board, shapeOptions)
            ogBoard = copy.deepcopy(board)
            if choiceIdx == None and location == None:
                continuePlay = False
                showPlay(ogBoard, board, shapeOptions, choiceIdx)
                endGame(board)
            
            board.placeShape(shapeOptions[choiceIdx], location)
            print("Move made: {}".format(moveCount))
            #showPlay(ogBoard, board, shapeOptions, choiceIdx)
            
            shapeOptions.pop(choiceIdx)


            moveCount += 1

            
    board.showBoard()
   
def endGame(board: Board):
    exit()
    
def showPlay(ogBoard: Board, newBoard: Board, ops: list, choice: int) -> None:
    print("*"*30)
    print("Board Before Move:")
    ogBoard.showBoard()
    print("")
    print("Shape options for move:")
    printShapes(ops)
    if choice is not None:
        print("Played Shape Number {}".format(choice + 1))
        print("Board After Move:")
        newBoard.showBoard()
    print("Score After Move: {}".format(newBoard.score))
    print("*"*30)
        
def printShapes(shapeList: list) -> None:
    
    paddedShapes = []
    maxX = 0
    maxY = 0
    for shape in shapeList:
        x, y = shape.shape
        maxX = max(maxX, x)
        maxY = max(maxY, y)
    
    for shape in shapeList:
        x, y = shape.shape
        paddedShapes.append(np.pad(shape, ((0, maxX-x),(0, maxY-y)), mode='constant'))
    
    bigArr = np.array(paddedShapes)
    for i in range(bigArr.shape[1]):
        printString = ""
        for j in range(bigArr.shape[0]):
            printString += np.array2string(bigArr[j, i, :]) + " "*5
        
        printString = printString.replace("[", "").replace("]", "")
        printString = printString.replace("1", "\u220e").replace("0", " ")
        
        print(printString)
    
if __name__ == "__main__":
    
    
    startGame()