n = int(input())
time_list = []
a_list = []
for i in range(n):
    input_list = list(map(int,input().split()))
    time = input_list[0]
    time_list.append(time)
    a = input_list[1:]
    a_list.append(a)
    
need = [False]*n
need[n-1] = True
for i in range(n,-1,-1):
    if need[i]:
        for j in a_list: need[j-1] = True
    
ans = 0
for i in range(n):
    if need[i]:
        ans += time_list[i]
print(ans)


    