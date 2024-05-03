q = int(input())
ans_list = []
for i in range(q):
    a,b = map(int,input().split())
    int_b = int(b)
    if a == 1:
        ans_list.append(b)
    elif a == 2:
        print(ans_list[-(b)])
        
        
        
