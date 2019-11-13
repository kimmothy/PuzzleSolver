class HeapNode:
    left = None
    right = None
    data = None

    def __init__(self,data):
        self. data = data

    def heapify(self):
        data = self.data
        if self.left is None and self.right is None:
            return
        elif self.right is None:
            if self.left.data < self.data:
                tmp = self.data
                self.data = self.left.data
                self.left.data = tmp
                self.left.heapify()
        else:
            if self.left.data < self.right.data:
                smaller = self.left
            else:
                smaller = self.right
            if self.data < smaller.data:
                return
            else:
                tmp = smaller.data
                smaller.data = self.data
                self.data = tmp
                smaller.heapify()

# 힙을 통해 구현한 우선순위 큐다
# 데이터를 넣거나 뺄 때 항상 루트 노드의 데이터가 우선순위가 높은 데이터가 오도록 해야한다
# 각 노드(서브트리의 루트) 도 자식 노드에 대해 그래야 한다.
class PriorityQueue:
    root = None
    length = 0
    depth = 0
 
    # add에서는 각 노드가 서브 노드보다 높은 우선순위를 유지할 수 있도록 data를 비교해가며 리프노드로 내려가야 한다
    def add(self, data):
        self.length += 1
        if self.length == 2**self.depth:
            self.depth += 1
        if self.length == 1:
            new_node = HeapNode(data)
            self.root = new_node
        else:
            # pointer는 힙을 타고 목표 리프노드까지 이동한다.
            # move_to_leaf는 목표 리프노드까지의 거리
            # path는 priority queue의 요소 갯수를 2진법으로 파악해 다음 요소가 들어갈 자리를 파악한다.
            pointer = self.root
            move_to_leaf = self.depth - 1
            path = self.length - (2**move_to_leaf)
            while True:
                # 각 노드의 데이터와 우선도와 추가할 데이터를 비교한다 만약 추가할 데이터의 우선도가 더 높다면
                # 해당 노드의 데이터와 교체하고 계속 내려가야 한다.
                if data < pointer.data:
                    tmp = pointer.data
                    pointer.data = data
                    data = tmp
                # move_to_leaf 노드가 1이라면 다음 노드는 새로운 데이터가 들어갈 리프노드, 즉 아직 존재하지 않는 노드
                # 따라서 moveToLeaf가 1일 때 이동을 멈추고 데이터를 넣어야 한다.
                if move_to_leaf == 1:
                    new_node = HeapNode(data)
                    if path == 0:
                        pointer.left = new_node
                    else:
                        pointer.right = new_node
                    break
                # path 
                move_to_leaf -= 1
                if path >= 2**move_to_leaf:
                    pointer = pointer.right
                    path -= 2**move_to_leaf
                else:
                    pointer = pointer.left

# get 메서드는 세 부분으로 이루어진다.
# 루트 노드에서 반환한 값을 빼내는 과정
# 힙의 끝에서 값을 받아와 빈 루트를 채우는 과정(완전 이진트리 형태를 유지하기 위해)
# 데이터 비교해가면서 우선순위 순서를 회복하는 과정
    def get(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            data= self.root.data
            self.root = None
            self.length = 0
            return data
        else:
            # 반환할 값을 미리 빼낸다.
            return_data = self.root.data
            self.root.data = None
            
            # 리프노드를 찾아가는 과정은 add와 동일하다
            pointer = self.root
            move_to_leaf = self.depth - 1
            path = self.length - (2 ** move_to_leaf)
            while True:
                # move_to_leaf 노드가 1이라면 다음 노드는 삭제되어야 할 리프노드이다.
                # 삭제될 리프 노드 에대한 참조를 해제하기 위해 moveToLeaf가 1일 때 멈추고 리프노드에 대한 참조를 삭제해야 한다.
                if move_to_leaf == 1:
                    if path == 0:
                        leaf_data = pointer.left.data
                        pointer.left = None
                    else:
                        leaf_data = pointer.right.data
                        pointer.right = None
                    break
                move_to_leaf -= 1
                if path >= 2 ** move_to_leaf:
                    pointer = pointer.right
                    path -= 2 ** move_to_leaf
                else:
                    pointer = pointer.left

            self.root.data = leaf_data
            self.length -= 1
            if self.length < 2**(self.depth-1):
                self.depth -= 1

            # 힙의 우선순위 회복과정은 특정 인덱스를 향하지 않는다.
            # 단지 좌우중 더 낮은 값을 찾아 값을 교환하며 이동할 뿐이다.
            # path가 필요하지 않기 때문에 node 클래스의 객체 메서드로 재귀적으로 해결할 수 있다.
            self.root.heapify()
            return return_data


if __name__ == "__main__":
    print("dd")
    q = PriorityQueue()
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(5)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(3)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(7)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(1)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(10)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(6)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(8)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    q.add(20)
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
    print(q.get())
    print(q.length,"데이터 양")
    print(q.depth,"데이터 깊이")
