import Queue

class Puzzle:
    state = [[]]
    field = [[[]]]
    visited = None
    puzzleQ = None
    def __init__(self, field, firstState):
        self.state = firstState
        self.field = field
        self.visited = Queue()
        self.puzzleQ = Queue()

    def getWays(self):
        pass

    def solve(self):
        ways = getWays()
        move = 0
        self.puzzleQ.enqueue({"ways":ways, "move":move})
        self.visited.enqueue({'state':state})
        while True:
            data = puzzleQ.dequeue()
            move = data["move"]
            move += 1
            states = nextQ["ways"]
            for s in States:
                self.state = s
                if isGoal():
                    return move
