from coding_practice.naver.PrintRequest import PrintRequest
from container.PriorityQueue import PriorityQueue


def solution(data):
    data_len = len(data)
    answer = []
    print_queue = PriorityQueue()
    complete_current_time = 0
    next_request_time = data[0][1]
    time = next_request_time
    while True:
        if len(answer) == data_len:
            break
        if data != [] and data[0][1] == time:
            new_request = PrintRequest(data.pop(0))
            print_queue.add(new_request)
        if print_queue.length != 0 and time >= complete_current_time:
            next_print = print_queue.get()
            answer.append(next_print.number)
            complete_current_time = time + next_print.pageNum
        time += 1

    return answer


if __name__ == "__main__":
    data = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]
    answer = solution(data)
    print(answer)