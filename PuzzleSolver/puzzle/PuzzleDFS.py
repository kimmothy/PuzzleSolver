from PuzzleSolver.puzzle.Stack import Stack

class PuzzleDFS:
    """
    field는 퍼즐판의 모양을 보여주는 다차원 리스트이다.

    두 숫자는 블럭의 좌측 상단 부분의 좌표를 나타낸다.
    goal은 게임을 끝마치기 위해 특정 블럭이 가야 할 자리이다.
    특정 블럭이란 blocks의 0번 블럭을 말하며, 좌측 상단의 좌표만 비교한다.
    direction은 "forward" 혹은 "back"으로 표현되며 최근에 스택에 데이터를 추가했는지, 혹은 빼냈는지 저장한다.
    정점과 간선이 정해지지 않은 상태에서 깊이 우선 탐색을 하기 때문에, 새로운 데이터를 추가한 뒤엔(direction이 "forward"일 때)
    해당 상황에서 연결될수 있는 간선(가능한 모든 블럭의 움직임)을 탐색해야 한다.
    """
    field = [[0,0],[0,0]]
    position = [[0,0],[0,0]]
    goal = [0,0]
    direction = None

    def __init__(self, firstPosition, goal, field=None):
        self.position = firstPosition
        self.field = field
        self.visited = Stack()
        self.puzzleS = Stack()
        self.goal = goal

    # getWays는 현재 위치에서 가능한 모든 종류의 이동을 구하기 위한 함수이다. 새로운 위치에 왔을 때
    # 간선을 구하기 위해 호출된다.

    def getWays(self):
        pass

    def solve(self):
        self.visited.append({"position":self.position})
        self.puzzleS.append({"position":self.position, "moveNum":0, "moveRecord":""})
        while True:
            data = self.puzzleS.pop()
            print(data)
            self.position = data["position"]
            moveNum = data["moveNum"] + 1
            moveRecord = data["moveRecord"]
            nextWays = self.getWays()
            print(nextWays,"rlf")
            for w in nextWays:
                newMove = w[0]
                newPosition = w[1]
                updatedRecord  = moveRecord + " " + newMove
                if self.goal(newPosition):
                    return updatedRecord, moveNum
                self.visited.append({"position":newPosition})
                self.puzzleS.append({"position":newPosition, "moveNum":moveNum, "moveRecord":updatedRecord})



if __name__ == "__main__":
    field = [[0,0,1,1,0,0],
             [0,0,1,1,0,0],
             [1,1,1,1,1,1],
             [1,1,1,1,1,1],
             [0,1,1,1,1,0],
             [0,1,1,1,1,0],
             [0,0,1,1,0,0],
             [0,0,1,1,0,0]]
