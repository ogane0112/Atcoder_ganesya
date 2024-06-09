from collections import deque
n = int(input())
a = deque(map(int,input().split()))

temp_list =deque(sorted(a)) 
temp_list.popleft()
check_first = temp_list[n//2]

temp_list =deque(sorted(a)) 
temp_list.pop()
check_second = temp_list[n//2]




for i in range(n):
    temp = a.popleft()
    if temp < check_second:
        print(check_second)
    else:
        print(check_first)
    a.append(temp)
    