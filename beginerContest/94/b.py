from collections import defaultdict
n,m,x = map(int,input().split())
am = list(map(int,input().split()))
d = defaultdict(int)
for i in range(n+1):
    if i in am:
        d[i] += 1
    else:  
        d[i] = 0
first_m = m
cost_n = 0
cost_0 = 0
for i in range(n+1):
    m += 1
    cost_n += d[i]
    if m == n+1:
        break
for i in range(n+1,-1,-1):
    m -= 1
    cost_0 += d[i]
    if m == 0:
        break   
print(min(cost_n,cost_0))