from container.Queue import Queue
from container.Stack import Stack


# state: 퍼즐의 변화하는 상태
# field: 퍼즐의 형태 state 변수가 퍼즐의 형태까지 담고있는 경우가 있어 기본값 None
# visited: 방문한 상태들을 기억하는 변수. __contains__가 잘 정의된 아무 객체나 사용 가능. 일단 queue를 사용
# container: 탐색을 위해 사용되는 자료구조. 초기화시 stack을 입력하면 깊이 우선 탐색이 되고, queue를 입력하면 너비우선 탐색이 된다.
# gaol: 퍼즐이 풀린 상태를 저장하는 lambda 변수. Puzzle을 상속하는 각 퍼즐 유형 클래스에서 별도의 함수로 정의하는 편이
# 더 바람직하지만 람다를 써보기 위해 변수로 정의했다.
class Puzzle:
    position = [[]]
    field = [[]]
    visited = None
    container = None
    goal = None  # lambda

    def __init__(self, firstPosition, goal, container, field = None):
        self.position = firstPosition
        self.field = field
        self.visited = Queue()
        # self.container = Queue() if container=="Queue" else Stack()
        if container == "Queue":
            self.container = Queue()
        elif container == "Stack":
            self.container = Stack()
        self.goal = goal

    # getWays는 Puzzle을 상속하는 각 퍼즐 유형에서 구현하애하는 함수다.
    # 퍼즐의 현 상태에서 가능한 모든 움직임을 찾아내는 기능을 수행해야 한다.
    # getWays의 반환값은 [(move, position), (move, position), ---]의 형태를 가져야 한다.
    # move는 프로그램 사용자에게 퍼즐의 변화를 보여주기 위한 문자열 타입이다. position은

    def getWays(self):
        pass

    def solve(self):
        self.container.add({"position":self.position, "moveNum":0, "moveRecord":""})
        self.visited.add({'position':self.position})
        while True:
            data = self.container.get()
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
                self.container.add({"position":newPosition, "moveNum":moveNum,"moveRecord":updatedRecord})
                self.visited.add({"position":newPosition})