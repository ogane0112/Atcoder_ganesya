a,m,l,r = map(int,input().split())
def cul(a,m,num):
    ans = (num-a)//m
    if (num-a)%m == 0 and ans >= 0 :
        ans += 1
    elif (num-a)%m == 0 and ans  <0:
        ans -= 1
    
    
    return ans 
#両方割り切れる場合テストケースに通らんな
min = cul(a,m,l)
max = cul(a,m,r)

print(max-min)