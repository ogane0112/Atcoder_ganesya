n = int(input())
d,x = map(int,input().split())
a = []
ans = 0
for i in range(n):
    a.append(int(input()))
ans += n
for i in range(1,n):
        while i+ (2*a[i]) >= d:
            ans+= 1
print(ans+x)   
