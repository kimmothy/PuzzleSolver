from puzzle.stack import stack

class Puzzle:
    """
    field는 블럭갈 수 있는 공간을 1, 갈 수 없는 공간을 0으로 나타내는 m*n 2차원 배열이다.
    blocks는 각 블록의 모양을 보여주는 변수다. blocks에 포함된 각 리스트는 각 블럭에 해당하며
    블럭에 포함된 튜플은 두 개의 숫자로 이뤄지며 블럭의 각 셀에 해당한다.
    해당 숫자는 블럭의 좌측 상단으로부터 각 셀의 상대 좌표이다.
    position은 블럭들의 위치를 나타내는 변수다. 각 리스트는 두개의 숫자를 가지고 있다.
    두 숫자는 블럭의 좌측 상단 부분의 좌표를 나타낸다.
    goal은 게임을 끝마치기 위해 특정 블럭이 가야 할 자리이다.
    특정 블럭이란 blocks의 0번 블럭을 말하며, 좌측 상단의 좌표만 비교한다.
    numOfBlocks는 말 그대로 블럭의 수다
    direction은 "forward" 혹은 "back"으로 표현되며 최근에 스택에 데이터를 추가했는지, 혹은 빼냈는지 저장한다.
    정점과 간선이 정해지지 않은 상태에서 깊이 우선 탐색을 하기 때문에, 새로운 데이터를 추가한 뒤엔(direction이 "forward"일 때)
    해당 상황에서 연결될수 있는 간선(가능한 모든 블럭의 움직임)을 탐색해야 한다.
    """
    field = [[0,0],[0,0]]
    blocks = [[(0,0)],[(0,0)]]
    position = [[0,0],[0,0]]
    goal = [0,0]
    numOfBlocks = 0
    direction = None

    def __init__(self, field, blocks, position, goal):
        self.field = field
        self.blocks = blocks
        self.position = position
        self.goal = goal
        self.numOfBlocks = len(blocks)
        self.direction = "forward"
    # getField는 현재 게임판의 블럭의 분포를 완전히 보여주는 함수다.
    # getWays 함수에서 블럭의 이동 가능성을 파악하기 위해 호출한다.
    def getField(self):
        current_field = self.field
        for i in range(self.numOfBlocks):
            block = blocks[i]
            for cell in block:
                # 블럭의 위치와, 블럭의 각 셀의 상대적 위치를 합하여 각 셀의 절대 위치 계산
                bPosition = self.position[i]
                cellrow = cell[0] + bPosition[0]
                cellcoll = cell[1] + bPosition[1]
                # 계산된 셀의 위치에 해당 블럭 정보를 입력
                # (0과 1은, 이동 불가능 지역과 가능 지역을 나타내기 때문에 2를 더한다.)
                current_field[cellrow][cellcoll] = i + 2
        return current_field
    # getWays는 현재 위치에서 가능한 모든 종류의 이동을 구하기 위한 함수이다. 새로운 위치에 왔을 때(direction이 forward일 때)
    # 간선을 구하기 위해 호출된다.
    def getWays(self):
        possible_ways = []
        current_field = self.getField()
        for i in range(self.numOfBlocks):
            block = blocks[i]
            rowmin, rowMax, colMin, colMax = len(current_field[0]), 0, len(current_field), 0
            for b in block:
                if b[0] < rowmin:
                    rowmin = b[0]
                elif b[0] > rowMax:
                    rowMax = b[0]
                if b[1] < colMin:
                    colMin = b[1]
                elif b[1] > colMax:
                    colMax = b[1]
            bWidth = rowMax - rowmin
            bHeight = colMax - colMin
            del rowmin, rowMax, colMin, colMax
            bPosition = self.position[i]
            bprow = bPosition[0]
            bpcoll = bPosition[1]
            exactBlock = [[row+bprow, coll+bpcoll] for [row,coll] in block]
            if bprow >0:
                left = [[row-1, coll] for [row,coll] in exactBlock]
                p = True
                for j in left:
                    moved = current_field[j[0]][j[1]]
                    if moved == 1 or moved == (i+2):
                        pass
                    else:
                        p = False
                        break
                if p == True:
                    possible_ways.append([i,"left"])
            if bprow+bWidth+1 < len(current_field[0]):
                right = [[row+1, coll] for [row,coll] in exactBlock]
                p = True
                for j in right:
                    moved = current_field[j[0]][j[1]]
                    if moved == 1 or moved == (i+2):
                        pass
                    else:
                        p = False
                        break
                if p == True:
                    possible_ways.append([i,"right"])
            if bpcoll >0:
                up = [[row, coll-1] for [row,coll] in exactBlock]
                p = True
                for j in up:
                    moved = current_field[j[0]][j[1]]
                    if moved == 1 or moved == (i+2):
                        pass
                    else:
                        p = False
                        break
                if p == True:
                    possible_ways.append([i,"up"])
            if bpcoll+bHeight+1 >len(current_field):
                down = [[row-1, coll] for [row,coll] in exactBlock]
                p = True
                for j in down:
                    moved = current_field[j[0]][j[1]]
                    if moved == 1 or moved == (i+2):
                        pass
                    else:
                        p = False
                        break
                if p == True:
                    possible_ways.append([i,"down"])
        return possible_ways

    def moveBack(self,moves):
        self.direction="back"
        reverseMove = moves.pop()["lm"]
        block = reverseMove[0]
        way = reverseMove[1]
        if way == "up":
            self.position[block][1] += 1
        elif way == "down":
            self.position[block][1] -= 1
        elif way == "left":
            self.position[block][0] += 1
        elif way == "right":
            self.position[block][0] -= 1

    def moveForward(self,move):
        print("움직ㅇㅆ어")
        print(move)
        way = move[1]
        block = move[0]
        self.direction = "forward"
        if way == "up":
            self.position[block][1] -= 1
        elif way == "down":
            self.position[block][1] += 1
        elif way == "left":
            self.position[block][0] -= 1
        elif way == "right":
            print("움직일뻔?")
            self.position[block][0] += 1

    def solution(self):
        visited = stack()
        moves = stack()
        lastMove = None
        while self.position[0] != goal:
            for m in moves:
                print("어떻게 왔지?",m)
            print("위치는?",self.position)
            if self.position in visited:
                self.moveBack(moves)
                continue
            if self.direction == "forward":
                visited.append(self.position)
                possibleWays = self.getWays()
                if possibleWays == []:
                    self.moveBack(moves)
                    continue
                else:
                    lastMove = possibleWays.pop(0)
                    moves.append({"lm":lastMove,"pw":possibleWays})
                    self.moveForward(lastMove)
            elif self.direction == "back":
                if lastMove.data["pw"] == []:
                    moveBack(moves)
                    continue
                else:
                    lastMove = moves.data["pw"].pop(0)
                    self.moveForward(lastMove)
        for m in moves:
            print(m)

field = [[0,0,1,1,0,0],
         [0,0,1,1,0,0],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1],
         [0,1,1,1,1,0],
         [0,1,1,1,1,0],
         [0,0,1,1,0,0],
         [0,0,1,1,0,0]]
position = [[0,2],[3,1],[3,3],[4,2],[4,3],[6,2]]
blocks = [[(0,0),(0,1),(1,0),(1,1)],[(0,0),(0,1),(1,1)],[(0,0),(0,1),(1,0)],[(0,0),(1,0),(1,1)],[(0,1),(1,0),(1,1)],[(0,0),(0,1)]]
goal = [6,2]

puzzle = Puzzle(field,blocks,position,goal)
puzzle.solution()