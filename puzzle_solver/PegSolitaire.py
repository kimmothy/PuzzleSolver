from puzzle_solver.Puzzle import Puzzle


class PegSolitaire(Puzzle):

    def getWays(self):
        ways = []
        rowNum = len(self.position)
        colNum = len(self.position[0])
        ps = self.position
        for r in range(rowNum):
            for c in range(colNum-2):
                if ps[r][c] + ps[r][c+1] + ps[r][c+2] == 2 and ps[r][c+1] == 1:
                    newPosition = []
                    for i in range(len(ps)):
                        newPosition.append(ps[i].copy())
                    newPosition[r][c] = 1 - newPosition[r][c]
                    newPosition[r][c+1] = 1 - newPosition[r][c+1]
                    newPosition[r][c+2] = 1 - newPosition[r][c+2]
                    if ["position", newPosition] in self.visited:
                        continue
                    ways.append(("(%d, %d H) " %(r, c), newPosition))

        for r in range(rowNum-2):
            for c in range(colNum):
                if ps[r][c] + ps[r+1][c] + ps[r+2][c] == 2 and ps[r+1][c] == 1:
                    newPosition = []
                    for i in range(len(ps)):
                        newPosition.append(ps[i].copy())
                    newPosition[r][c] = 1 - newPosition[r][c]
                    newPosition[r+1][c] = 1 - newPosition[r+1][c]
                    newPosition[r+2][c] = 1 - newPosition[r+2][c]
                    if ["position", newPosition] in self.visited:
                        continue
                    ways.append(("(%d, %d V) " %(r, c), newPosition))

        return ways


if __name__ == "__main__":

    firstPosition = [[3, 3, 0, 0, 0, 3, 3],
                     [3, 3, 0, 0, 0, 3, 3],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [3, 3, 1, 1, 1, 3, 3],
                     [3, 3, 1, 1, 1, 3, 3]
                     ]
    goal = lambda position: position == [[3, 3, 0, 0, 0, 3, 3],
                                         [3, 3, 0, 0, 0, 3, 3],
                                         [0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 1, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0],
                                         [3, 3, 0, 0, 0, 3, 3],
                                         [3, 3, 0, 0, 0, 3, 3]
                                         ]

    container = "Stack"
    # container = "Queue"
    myPuzzle = PegSolitaire(firstPosition, goal, container)
    moving, moveNum = myPuzzle.solve()

    print("이동횟수",moveNum)
    print("이동경로", moving)
