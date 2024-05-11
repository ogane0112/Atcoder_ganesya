from heapq import heapify,heappop,heappush
n,m = map(int,input().split())

route = [[] for i in range(m)]

for i in range(m):
    a,b,w = map(int,input().split())
    route[a-1].append((b-1,w))
    route[b-1].append((a-1,w))


start = 0

q = [0,start]
dist = [float("inf")] * n
check = [False] * n
dist[start] = 0


