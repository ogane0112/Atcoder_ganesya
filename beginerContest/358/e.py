k= int(input())
C = list(map(int, input().split()))
MOD = 998244353

fact = [1] * (k+ 1)
for i in range(K):
    fact[i + 1] = fact[i] * (i + 1) % mod
ifact = [1] * (k+ 1)
ifact[k] = pow(fact[k], -1, mod)
for i in range(K, 0, -1):
    ifact[i - 1] = ifact[i] * i % mod


def c(n, r):
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD
dp = [[0]*(K+1)for _ in range(len(C+1hs))]