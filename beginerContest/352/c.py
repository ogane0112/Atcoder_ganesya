# 入力を受け取る
from itertools import combinations
n, k = map(int, input().split())
p = list(map(int, input().split()))
nums = [i+1 for i in range(n)]
#住所録を作成する
a = []
ans_list = []
for i in range(n):
    a.append(p.index(i+1))

#ここで差を計算する
for start in range(n - k + 1):
    subseq = nums[start:start + k]
    ans_list.append(a[start+k]-a[start])

print((ans_list))

def is_good_index(P, K, start):
    """
    P[start], P[start+1], ..., P[start+K-1] の中に連続するK個の整数が含まれ、かつその差がK-1以下であるかを判定する。
    """
    values = sorted(P[start:start+K])
    if values[-1] - values[0] <= K - 1:
        return True
    return False

def solve(P, K):
    N = len(P)
    P.sort()  # 昇順に並び替え

    # 二分探索で最小のiを探す
    left, right = 0, N - K
    while left <= right:
        mid = (left + right) // 2
        if is_good_index(P, K, mid):
            right = mid - 1
        else:
            left = mid + 1

    return K - 1

# 入力例
N, K = map(int, input().split())
P = list(map(int, input().split()))

print(solve(P, K))  # 出力: 5
