n,m =  map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
x = [0]*n
flag = True
for i in range(m):
    if a_list[i]==b_list[i]:
        flag = False
        break
    else:
        if x[a_list[i]]==0 and x[b_list[i]]==0:
            x[a_list[i]]=1
        elif (x[a_list[i]]==0 and x[b_list[i]]==1) or (x[a_list[i]]==0 and x[b_list[i]]==1) :
            continue
        elif  x[a_list[i]]==1 and x[b_list[i]]==1:
            flag = False
            break 




if flag:
    print("Yes")
else:
    print("No")