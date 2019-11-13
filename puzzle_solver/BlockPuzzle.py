from puzzle_solver.Puzzle import Puzzle

class BlockPuzzle(Puzzle):
    def isValidate(self, newPosition, movedBlockIndex):
        rowNum = len(self.field)
        colNum = len(self.field[0])
        block = newPosition[movedBlockIndex]
        if ["position", newPosition] in self.visited:
            return False
        for cell in block:
            if cell[0] < 0 or cell[0] >= rowNum:
                return False
            elif cell[1] < 0 or cell[1] >= colNum:
                return False
            elif self.field[cell[0]][cell[1]] == 0:
                return False
            for otherIndex, otherBlock in enumerate(newPosition):
                if otherIndex == movedBlockIndex:
                    continue
                elif cell in otherBlock:
                    return False
        return True

    def getWays(self):
        ways = []
        up = lambda x: [x[0]-1, x[1]]
        down = lambda x: [x[0]+1, x[1]]
        left = lambda x: [x[0], x[1]-1]
        right = lambda x: [x[0], x[1]+1]
        directions = {"up":up, "down": down, "left":left, "right":right}
        for index, block in enumerate(self.position):

            for d in directions.keys():
                newPosition = self.position.copy()
                movedBlock = list(map(directions[d], block))
                newPosition[index] = movedBlock
                if self.isValidate(newPosition, index):
                    recordMove = str(index) + d
                    ways.append((recordMove, newPosition))

        return ways



if __name__ == "__main__":
    field = [[0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             ]
    firstPosition = [[[0, 2], [0, 3], [1, 2], [1, 3]],
             [[3, 1], [3, 2], [4, 2]],
             [[3, 3], [3, 4], [4, 3]],
             [[4, 1], [5, 1], [5, 2]],
             [[4, 4], [5, 3], [5, 4]],
             [[6, 2], [6, 3]]
             ]
    goal = lambda position: position[0][0] == (6,2)
    # container = "Stack"
    container = "Queue"

    myPuzzle = BlockPuzzle(firstPosition, goal, container, field)
    moving, moveNum = myPuzzle.solve()
    print("이동횟수",moveNum)
    print("이동경로", moving)