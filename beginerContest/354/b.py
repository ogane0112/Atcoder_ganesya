from collections import defaultdict
n = int(input())
d  = []
sum = 0
for i in range(n):
    s,c = map(str,input().split())
    sum += int(c)
    d.append((s,int(c)))
check = sum%n
if  check == 0:
       print(d[n-1])
else:
    print(d[n-1])