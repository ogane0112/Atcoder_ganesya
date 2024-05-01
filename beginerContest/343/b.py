n = int(input())
g_list = []
ans_list = []

for i in range(n):
    temp_list =  list(map(int,input().split()))
    g_list.append(temp_list)

for i in range(n):
    for j in range(n):
       
        if g_list[i][j] == 1 and j ==n:
        
            print(j+1)
            
        elif g_list[i][j] == 1:
            
            print(j+1,end = " ")
            
        elif j == n:
            print("\n")
            
            
            
    