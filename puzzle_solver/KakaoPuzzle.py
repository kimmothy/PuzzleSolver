from puzzle_solver.Puzzle import Puzzle


class PegSolitaire(Puzzle):

    def getWays(self):

        return ways


if __name__ == "__main__":
    field = [[0, 0, 0, 1, 1],
             [0, 0, 0, 1, 0],
             [0, 1, 0, 1, 1],
             [1, 1, 0, 0, 1],
             [0, 0, 0, 0, 0]]
    firstPosition = [[0, 0], [0, 1]]
    goal = lambda position, n: position.count(n) == 3
    container = "Queue"
    myPuzzle = PegSolitaire(firstPosition, goal, container, field)
    moving, moveNum = myPuzzle.solve()
    print("이동횟수",moveNum)
    print("이동경로", moving)
