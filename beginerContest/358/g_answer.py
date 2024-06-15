#!/usr/bin/env python3

INF = 1 << 60

H, W, K = map(int, input().split())

si, sj = map(int, input().split())
si -= 1
sj -= 1

A = [list(map(int, input().split())) for _ in range(H)]

# (i, j)に到達するまでに同じところを通らずにk回移動した時の、得点の最大値
dp = [[[-INF] * (H * W + 1) for _ in range(W)] for _ in range(H)]

dp[si][sj][0] = 0

for k in range(H * W):
    for i in range(H):
        for j in range(W):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                dp[ni][nj][k + 1] = max(dp[ni][nj][k + 1], dp[i][j][k] + A[ni][nj])

res = 0

for i in range(H):
    for j in range(W):
        for k in range(H * W + 1):
            if dp[i][j][k] == -INF:
                continue
            if K - k >= 0:
                res = max(res, dp[i][j][k] + A[i][j] * (K - k))

for i in range(H):
    for j in range(W):
        if K <= H * W:
            res = max(res, dp[i][j][K])

print(res)