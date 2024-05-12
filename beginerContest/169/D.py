#エラトステネスの篩で実装する
x = int(input())
ans = 0
#すべて素数だと
a = [True] * (x+1)
a[1], r = False, []

for i in range(1, x+1):
    if a[i]:
      if i <= x**0.5:
        for j in range(i*i, x+1, i):
          a[j] = False
      r += [i]

for i in r:
  for j in range(1,10000):
    if x%(i**j) != 0:
      break
    elif x == 1:
      break
    x = x//(i**j)
    ans += 1
print(ans)