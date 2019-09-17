class stackNode:
    link = None
    data = {}

    def __init__(self,data, link=None):
        self.link = link
        self.data = data


class Stack:
    top = None

    def __init__(self):
        self.top = None

    def __iter__(self):
        return StackIterator(self)

    def __contains__(self, item):
        key = item[0]
        value = item[1]
        try:
            for q in self:
                if q[key] == value:
                    return True
        except StopIteration:
            return False

    def pop(self):
        if self.top is None:
            return None
        else:
            tmp = self.top.data
            self.top = self.top.link
            return tmp

    def append(self, data):
        newNode = stackNode(data)
        newNode.link = self.top
        self.top = newNode


class StackIterator:
    indexPoint = None

    def __init__(self, stack):
        self.indexPoint = stack.top

    def __next__(self):
        if self.indexPoint is None:
            raise StopIteration
        else:
            tmp = self.indexPoint.data
            self.indexPoint = self.indexPoint.link
            return tmp