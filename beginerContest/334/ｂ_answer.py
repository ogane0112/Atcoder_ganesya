a,m,l,r = map(int,input().split())
def cul(a,m,num):
    ans = (num-a)//m  
    return ans 
def check(a,m,num):
    ans = (num-a)%m  
    return ans 
    
#両方割り切れる場合テストケースに通らんな
min = cul(a,m,l)
max = cul(a,m,r)

check_min = check(a,m,l)
check_max = check(a,m,l)

if check_min==0 or check_max==0:
    print(max-min+1)
else:
    print(max-min)