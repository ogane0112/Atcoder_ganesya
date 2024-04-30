import math
n = int(input())
xy_list = []
temp_list = []
count = 0

def cul(x1,x2,y1,y2):
    x = (x1-x2)**2
    y = (y1-y2)**2
    return math.sqrt(x+y)
    
for i in range(n):
    x,y = map(int,input().split())
    xy_list.append((x,y))

#全てのユークリッド距離を求める
for x1 ,y1 in xy_list:
    for  x2,y2 in xy_list:
        temp =  cul(x1,x2,y1,y2)
        temp_list.append(temp)
        count += 1
        if count == n:
            ans = temp_list.index(max(temp_list))  
            print(ans+1)
            temp_list = []
            count = 0
            
        