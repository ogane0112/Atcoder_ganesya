from collections import defaultdict
d = defaultdict(list)
n = int(input())
ans_list= []
for i in range(n):
    a ,c= map(int,input().split())
    d[c].append(a)
    
for value in d.values():
    ans_list.append(min(value))

print(max(ans_list))
    
    
    
    
    
    
    