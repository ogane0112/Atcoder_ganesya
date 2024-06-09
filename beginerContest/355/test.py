n = int(input())
field = []
def check(field,cx,cy):
    check = []
    for i in field:
        x,y,h = i
        H = h+abs(x-cx)-abs(y-cy)
        check.append(H)
    
    return check
for i in range(n):
    x,y,h = map(int,input().split())
    field.append((x,y,h))

for i in range(100):
    for j in range(100):
        if len(list(set(check(field,i,j)))) == 1:
            ans = check(field,i,j)
            print(f"{i} {j} {ans[0]}")
            break
                