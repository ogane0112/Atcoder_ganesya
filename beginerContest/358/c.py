from itertools import combinations

# 入力の読み込み
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
bitMask = [0]*N
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            #or演算する
            bitMask[i] |= 1 << j
            
ans= N #最大の売り場の数
#1種類ずつ調べていく
for r in range(1,N+1):
    for combo in combinations(range(N),r):
        check = 0
        for i in combo:
            check |= bitMask[i]
        #このコードは"1"*mになっているか確かめる用のコード
        if check == (1<<M) -1:
            ans = min(ans,r)
            break
            
print(ans)
    