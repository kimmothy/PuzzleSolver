from PuzzleSolver.puzzle.Queue import Queue


class PuzzleBFS:
    state = [[]]
    field = [[[]]]
    visited = None
    puzzleQ = None
    goal = None#lambda

    def __init__(self, firstPosition, goal, field = None):
        self.position = firstPosition
        self.field = field
        self.visited = Queue()
        self.puzzleQ = Queue()
        self.goal = goal

    # def getWays(self):
    #     pass

    def solve(self):
        self.puzzleQ.enqueue({"position":self.position, "moveNum":0, "moveRecord":""})
        self.visited.enqueue({'position':self.position})
        while True:
            data = self.puzzleQ.dequeue()
            print(data)
            self.position = data["position"]
            moveNum = data["moveNum"] + 1
            moveRecord = data["moveRecord"]
            nextWays = self.getWays()
            for w in nextWays:
                newMove = w[0]
                newPosition = w[1]
                updatedRecord = moveRecord + " " + newMove
                if self.goal(newPosition):
                    return updatedRecord, moveNum
                self.puzzleQ.enqueue({"position":newPosition, "moveNum":moveNum,"moveRecord":updatedRecord})
                self.visited.enqueue({"position":newPosition})


if __name__ == "__main__":
    firstPosition = [[]]
    field = [[]]
    goal = lambda position: position == [[]]