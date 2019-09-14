from PuzzleSolver.puzzle.PuzzleBFS import PuzzleBFS
from PuzzleSolver.puzzle.PuzzleDFS import PuzzleDFS


class KnightPuzzle:
    def isValidate(self, newPosition, movedBlockIndex):
        pass
    def getWays(self):
        rowNum = len(self.position[1])
        colNum = len(self.position[1][0])
        ways = []
        knightPosition = self.position[0]
        cloack1 = [knightPosition[0] -2, knightPosition[1] +1]
        cloack2 = [knightPosition[0] -1, knightPosition[1] +2]
        cloack4 = [knightPosition[0] +1, knightPosition[1] +2]
        cloack5 = [knightPosition[0] +2, knightPosition[1] +1]
        cloack7 = [knightPosition[0] +2, knightPosition[1] -1]
        cloack8 = [knightPosition[0] +1, knightPosition[1] -2]
        cloack10 = [knightPosition[0] -1, knightPosition[1] -2]
        cloack11 = [knightPosition[0] -2, knightPosition[1] -1]
        directions = [cloack1, cloack2, cloack4, cloack5, cloack7, cloack8, cloack10, cloack11]
        for d in directions:
            row = d[0]
            col = d[1]
            field = self.position[1]
            if row < 0 or row >= rowNum:
                continue
            elif col < 0 or col >= colNum:
                continue
            elif field[row][col] == 1:
                continue
            move = "(%d행 %d열로 이동)" %(row, col)
            newField = []
            for f in field:
                newField.append(f.copy())
            newField[row][col] = 1
            ways.append((move, [[row,col],newField]))
        return ways

class KnightPuzzleBFS(KnightPuzzle, PuzzleBFS):
    pass

class KnightPuzzleDFS(KnightPuzzle, PuzzleDFS):
    pass

if __name__ == "__main__":
    #앞의 두칸짜리 리스트는 나이트의 위치, 뒤의 2차원 배열은 판의 상태
    firstPosition = [ [0,0],
        [[1, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    ]
    goal = lambda position: position[1] == [[1 for x in range(3)] for y in range(4)]
    myPuzzle = KnightPuzzleBFS(firstPosition, goal)
    # myPuzzle = KnightPuzzleDFS(firstPosition, goal)
    moving, moveNum = myPuzzle.solve()
    print(moveNum)
    print(moving)