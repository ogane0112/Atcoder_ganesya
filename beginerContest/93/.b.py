a,b,k = map(int,input().split())
check = []
for i in  range(a,b+1):
    check.append(i)
check_sort = sorted(check)
ans1 = check_sort[:k]
ans2 = check_sort[-k:]



    
ans = list(set(ans1+ans2))
for i in ans:
    print(i)

    
    

  
    