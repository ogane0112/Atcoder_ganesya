n  = int(input())
p_list = list(map(int,input().split()))
q  = int(input())
for i in range(q):
    a,b = map(int,input().split())
    temp_a = p_list[a-1]
    temp_b = p_list[b-1]
    
    if  p_list[a-1]  > n//2:
        temp_a = abs(n-p_list[a-1])
        
    if  p_list[b-1] > n//2:
        temp_b = abs(n-p_list[b-1])
        
    if  temp_a < temp_b:
        print(a)
    else:
        print(b)
              