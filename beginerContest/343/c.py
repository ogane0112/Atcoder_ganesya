n = int(input())
def check(n):
    n_list = list(str(n))
    return n_list == n_list[::-1]

num = int(n**(1/3))+1

for i in range(num,-1,-1):
     temp = (i**(3))
     if check(temp) and temp <= n:
            print(temp)
            break
        
        
    