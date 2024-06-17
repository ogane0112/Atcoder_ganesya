from ganesya import UnionFind
n,m = map(int,input().split())
uf = UnionFind(n)
for i in range(m):
    a,b = map(int,input().split())
    uf.union(a-1, b-1)
print(uf.all_group_members)
    

    