class CombinationCalculator:
    def __init__(self, r, mod=998244353):
        self.r = r
        self.mod = mod
        self.fact = [1] * (r + 1)
        self.ifact = [1] * (r + 1)
        self._precompute_factorials()

    def _precompute_factorials(self):
        for i in range(self.r):
            self.fact[i + 1] = self.fact[i] * (i + 1) % self.mod
        self.ifact[self.r] = pow(self.fact[self.r], -1, self.mod)
        for i in range(self.r, 0, -1):
            self.ifact[i - 1] = self.ifact[i] * i % self.mod

    def comb(self, n, k):
        if k > n or k < 0:
            return 0
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n - k] % self.mod

# 使用例
r = int(input("rの値を入力してください: "))
calculator = CombinationCalculator(r)
n = int(input("nの値を入力してください: "))
k = int(input("kの値を入力してください: "))
print(f"comb({n}, {k}) = {calculator.comb(n, k)}")