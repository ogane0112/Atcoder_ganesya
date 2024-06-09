n,m = map(int,input().split())
h = list(map(int,input().split()))
count = 0
for i in range(n):
    m -= h[i]
    count += 1
    if m <= 0:
        break
print(count)