n,a = map(int,input().split())
t = list(map(int,input().split()))
total = 0
for i in range(n):
    if total <=  t[i]:
        total = t[i] + a
    else:
        total += a
    print(total)
    