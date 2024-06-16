import sys
from sortedcontainers import SortedList

def min_cost(n, m, a, b):
    # 配列をソート
    items = SortedList(a)
    requirements = sorted(b, reverse=True)

    if len(items) < m:
        return -1

    total_cost = 0

    for requirement in requirements:
        index = items.bisect_left(requirement)
        if index == len(items):
            return -1
        total_cost += items[index]
        items.pop(index)

    return total_cost

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    b = list(map(int, data[2+n:2+n+m]))

    result = min_cost(n, m, a, b)
    print(result)
