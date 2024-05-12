def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
n = int(input())
a = factorization(n) 
print(a)
ans = 0
num = len(a)
count = 0
for i in a:
    for j in range(1,10**9):
        if n%(i[0]**j) != 0:
            break
        elif n == 1:
            break
        n = n//(i[0]**j)
        ans += 1
print(ans)
        
    

    

