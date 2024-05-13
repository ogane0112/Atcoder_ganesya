n,k = map(int,input().split())
c = list(map(int,input().split()))
r = list(map(int,input().split()))
ans = 0
for i in range(n):
  if c[i] == k:
    if ans < r[i]:
      ans = i+1
      
print(ans)