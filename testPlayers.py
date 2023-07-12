from board import Board
from shapes import getRandomShape
from Players.dumbPlayer import DumbPlayer
from Players.midPlayer import MidPlayer
from Players.players import Player

class Result():
    def __init__(self, moves, score) -> None:
        self.moves = moves
        self.score = score
        
        
class TestResults():
    def __init__(self, name: str) -> None:
        self.playerName = name
        self.results = []
        
    def addResult(self, res: Result) -> None:
        self.results.append(res)
        
    def other(self, res) -> None:
        print("gggggggggg")
        
    def showResults(self, long: bool = True) -> None:
        if long:
            for i, res in enumerate(self.results):
                print("Game {}: Moves:{} Score:{}".format(i+1, res.moves, res.score))
        else:
            totalScore = 0
            totalMoves = 0
            for res in self.results:
                totalScore += res.score
                totalMoves += res.moves
            gamesNum = len(self.results)
            
            print("Over {} Games:".format(gamesNum))
            print("\tAverage Number of Moves: {}".format(totalMoves/gamesNum))
            print("\tAverage Score: {}\n".format(totalScore/gamesNum))
    
    def showResultsInline(self) -> None:
        totalScore = 0
        totalMoves = 0
        for res in self.results:
            totalScore += res.score
            totalMoves += res.moves
        gamesNum = len(self.results)
        print("{:11}|{:5}|{:9}|{:9}".format(self.playerName, gamesNum, round(totalMoves/gamesNum, 1), round(totalScore/gamesNum, 1)))
            
            


def runTest(board: Board, player: Player) -> Result:

    while True:
        shapeOptions = [getRandomShape() for j in range(3)]

        while len(shapeOptions) > 0: 
            choiceIdx, location = player.decideMove(board, shapeOptions, True)
            
            if choiceIdx == None and location == None:
                return Result(board.moves, board.score)
            
            board.placeShape(shapeOptions[choiceIdx], location)
            
            shapeOptions.pop(choiceIdx)


if __name__ == "__main__":
    
    dumbPlayer = DumbPlayer()
    dumbPlayerResults = TestResults("Dumb")
    midPlayer = DumbPlayer()
    midPlayerResults = TestResults("Mid")
    
    
    for i in range(10):
        dumbPlayerResults.addResult(runTest(Board(), dumbPlayer))
    
    for i in range(10):
        midPlayerResults.addResult(runTest(Board(), midPlayer))
    
    print("--------------------------------------")
    print("Player Type|Games|Avg Moves|Avg Score")
    print("-----------|-----|---------|----------")
    dumbPlayerResults.showResultsInline()
    midPlayerResults.showResultsInline()