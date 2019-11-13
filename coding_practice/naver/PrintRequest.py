class PrintRequest:
    number = 0
    requestTime = 0
    pageNum = 0

    def __init__(self, request):
        self.number = request[0]
        self.requestTime = request[1]
        self.pageNum = request[2]

    def __lt__(self, other):
        if self.pageNum == other.pageNum :
            return self.requestTime < other.requestTime
        else:
            return self.pageNum < other.pageNum


if __name__ == "__main__":
    a = PrintRequest([1, 2, 10])
    b = PrintRequest([2, 3, 5])
    c = PrintRequest([3, 4, 5])
    print(a)