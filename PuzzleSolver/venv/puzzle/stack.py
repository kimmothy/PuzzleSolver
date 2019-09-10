class stackNode:
    link = None
    data = None

    def __init__(self, link, data):
        self.link = link
        self.data = data

    def pop(self):
        return self.link

    def append(self, data):
        newStack = stackNode(self, data)
        return newStack

class stack:
    lastPoint = None
    indexPoint = None

    def __init__(self):
        self.lastPoint = None

    def __iter__(self):
        return stackIterator(self)

    def __contains__(self, item):
        try:
            for i in self:
                if i == item:
                    return True
        except StopIteration:
            return False

    def pop(self):
        if self.lastPoint == None:
            return None
        else:
            tmp = self.lastPoint.data
            self.lastPoint = self.lastPoint.pop()
            return tmp
    def getData(self):
        return self.lastPoint.data

    def append(self, data):
        if self.lastPoint == None:
            self.lastPoint = stackNode(None, data)
        else:
            self.lastPoint = self.lastPoint.append(data)

class stackIterator:
    indexPoint = None

    def __init__(self, stack):
        self.indexPoint = stack.lastPoint

    def __next__(self):
        if self.indexPoint == None:
            raise StopIteration
        else:
            tmp = self.indexPoint.data
            self.indexPoint = self.indexPoint.link
            return tmp