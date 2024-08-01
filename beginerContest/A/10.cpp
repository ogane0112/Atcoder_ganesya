n=int(input())

check = [100,200,300,400]
for i in check:
    if i-n>0:
        ans = i - n
        break
print(ans)