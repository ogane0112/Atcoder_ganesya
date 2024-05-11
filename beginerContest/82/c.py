from collections import defaultdict
d = defaultdict(int)
n = int(input())
a_list = map(int,input().split())

for i in range(n):
    d[i+1] = a_list.count(i+1)
