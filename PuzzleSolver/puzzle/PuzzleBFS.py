from PuzzleSolver.puzzle.queue import Queue


class Puzzle:
    state = [[]]
    field = [[[]]]
    visited = None
    puzzleQ = None
    goal = None#lambda

    def __init__(self, field, firstPosition, goal):
        self.position = firstPosition
        self.field = field
        self.visited = Queue()
        self.puzzleQ = Queue()
        self.goal = goal

    def getWays(self):
        pass

    def solve(self):
        moveNum = 0
        moveRecord = ""
        self.puzzleQ.enqueue({"position":self.position, "moveNum":moveNum, "moveRecord":moveRecord})
        self.visited.enqueue({'state':self.state})
        while True:
            data = self.puzzleQ.dequeue()
            moveNum = data["moveNum"] + 1
            moveRecord = data["moveRecord"]
            self.position = data["position"]
            ways = self.getWays()
            for w in ways:
                newMove = w[0]
                newPosition = w[1]
                updatedRecord = moveRecord + newMove
                self.puzzleQ.enqueue({"position":newPosition, "moveNum":moveNum,"moveRecord":updatedRecord})
                if self.goal():
                    return updatedRecord, moveNum

if __name__ == "__main__":
    firstPosition = [[]]
    field = [[]]
    goal = lambda position: position[0] == (6,2)