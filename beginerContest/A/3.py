n = int(input())

def cul(x,num):
  result = 0
  for i in range(x):
    result += num
    
  return result
ans = 0
for i in range(1,n+1):
  ans += cul(i,10000)
  
print(ans//n)