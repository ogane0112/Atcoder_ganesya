import bisect
n,q = map(int,input().split())
r_list = list(map(int,input().split()))
sort_list = sorted(r_list)
for i in range(n-1):
    sort_list[i+1] += sort_list[i]
    
for i in range(q):
    x = int(input())
    ans = bisect.bisect_right(sort_list,x)
    print(ans)
    