#漸化式１のメモ再帰を利用した実装コード
n  = int(input())
def memo_sample(n):
  dict = {}
  if n == 0 or n == 1:
    dict[n]=1
    return 1
  if n in dict.keys():
    
    return dict[n]
  dict[n] =  memo_sample(n-1) + 2
  return dict[n]

ans = memo_sample(n)
print(ans)