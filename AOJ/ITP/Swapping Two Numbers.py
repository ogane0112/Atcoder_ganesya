for i in range(10000):
        xy_list = list(map(int,input().split()))
        xy_list.sort()
        if xy_list[0] == 0 and xy_list[1] == 0:
            break
        print(*xy_list)
        
        
        
        
    