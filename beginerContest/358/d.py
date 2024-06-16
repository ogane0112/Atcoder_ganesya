#貪欲法で解く
n,m = map(int,input().split())
a =list(map(int,input().split()))
b = list(map(int,input().split()))

a = a.sorted()
b.sorted(reversed=True)
#可能かどうかの判定をする
for i in range(m):
    
    
    