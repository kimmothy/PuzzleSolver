from PuzzleSolver.puzzle.Stack import Stack


# 클래스 PuzzleDFS는 깊이 우선탐색으로, 퍼즐을 풀어나가는 클래스이다. 퍼즐의 상태를 변수로 갖는다.
class PuzzleDFS:
    """
    field는 퍼즐판의 모양을 보여주는 다차원 리스트이다. 대체로 2차원 리스트로 표현된다. getWays() 메서드에서 사용된다.
    position은 퍼즐의 상태를 나타내는 변수다. 퍼즐의 종류에 따라 다른 형태로 사용된다.  getWays()메서드에서 사용된다.
    position이 퍼즐의 형태를 보여줄만한 경우라면, field는 None으로 두고 position만으로 getWays()를 시행한다.
    goal은 게임을 끝마치기 위한 조건이다. lambda 문법을 사용한다.
    """
    state = [[]]
    field = [[]]
    visited = None
    puzzleS = None
    goal = None  # lambda

    def __init__(self, firstPosition, goal, field=None):
        self.position = firstPosition
        self.field = field
        self.visited = Stack()
        self.puzzleS = Stack()
        self.goal = goal

    # getWays는 현재 위치에서 가능한 모든 종류의 이동을 구하기 위한 함수이다. 새로운 위치에 왔을 때
    # 가능한 움직임을 구하기 위해 호출된다.
    # 각 퍼즐들이 구현해야 할 부분이다.
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
            for w in nextWays:
                newMove = w[0]
                newPosition = w[1]
                updatedRecord = moveRecord + " " + newMove
                if self.goal(newPosition):
                    return updatedRecord, moveNum
                self.visited.append({"position":newPosition})
                self.puzzleS.append({"position":newPosition, "moveNum":moveNum, "moveRecord":updatedRecord})
