n,q= map(int,input().split())
s = input()
s_list = list(s)
for  i in range(q):
    count= 0
    l,r = map(int,input().split())
    temp_list = s_list[l-1:r-1]
    for j in range(len(temp_list)-1):
        if temp_list[j] == temp_list[j+1]:
            count += 1
    print(count)
    
