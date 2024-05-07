n,x = map(int,input().split())
s_list = list(map(int,input().split()))
ans = 0
for i in s_list:
    if i <=x:
        ans +=i

print(ans)