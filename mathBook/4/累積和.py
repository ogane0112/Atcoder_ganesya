n,q = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n-1):
    a[i+1] += a[i]
a.insert(0,0)
for i in range(q):
    l,r = map(int,input().split())
    print(a[r]-a[l-1])
    
print(a)