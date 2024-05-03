n  = int(input())
p_list = list(map(int,input().split()))
q  = int(input())
for i in range(q):
    a,b = map(int,input().split())
    temp_a = p_list.index(a)
    temp_b = p_list.index(b)

        
        
    if  temp_a < temp_b:
        print(a)
    else:
        print(b)
              