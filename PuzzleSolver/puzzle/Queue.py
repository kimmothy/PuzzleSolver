class Node:
    link = None
    data = {}

    def __init__(self,data, link=None):
        self.link = link
        self.data = data


class Queue:
    bottom = None
    top = None

    def __init__(self):
        self.bottom = None
        self.top = None

    def __iter__(self):
        return QueueIterator(self)

    def __contains__(self, item):
        key = item[0]
        value = item[1]
        try:
            for q in self:
                if q[key] == value:
                    return True
        except StopIteration:
            return False

    def enqueue(self, data):
        newNode = Node(data)
        if self.top == None:
            self.top = newNode
            self.bottom = newNode
        else:
            self.top.link = newNode
            self.top = newNode

    def dequeue(self):
        if self.bottom == None:
            return None
        else:
            tmp = self.bottom
            self.bottom = tmp.link
            if tmp.link == None:
                self.top = None
            return tmp.data


class QueueIterator:
    pointer = None
    def __init__(self, queue):
        self.pointer = queue.bottom

    def __next__(self):
        if self.pointer == None:
            raise StopIteration
        data = self.pointer.data
        self.pointer = self.pointer.link
        return data