n = int(input())
a_list = list(map(int,input().split()))

dp1 = [0]*1000000
dp2 = [0]*1000000

dp1[0] = 0
dp2[0] = 0

for i in range(1,n+1):
    dp1[i] = dp2[i]+a_list[i-1]
    dp2[i] = max(dp1[i-1],dp2[i-2]) 

print(max(dp1[n],dp2[n]))

    