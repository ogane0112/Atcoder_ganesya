k = int(input())
c = list(map(int, input().split()))
mod = 998244353
fact = [1] * (k+ 1)
for i in range(k):
    fact[i + 1] = fact[i] * (i + 1) % mod
ifact = [1] * (k+ 1)
ifact[k] = pow(fact[k], -1, mod)
for i in range(k, 0, -1):
    ifact[i - 1] = ifact[i] * i % mod
def comb(n, r):
    return fact[n] * ifact[r] % mod * ifact[n - r] % mod
def swap(a,b):
    temp = a
    a = b
    b = temp
#a~zまでの個数
n = 26

dp = [0]*(k+1)
old = [0]*(k+1)
#長さが0の物が一つできる
dp[0] = 1

for i in range(n):
    #oldとdpの値を交換する
    swap(old,dp)
    for j in range(k+1):
        for a in range(c[i]+1):
            nj = j+a
            if nj > k : break
            dp[nj] += old[j] * comb(nj,a)
ans = 0
for i in range(k):
    ans += dp[i+1]
print(ans)
print(dp)