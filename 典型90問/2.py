# カッコ列 S が整合しているかどうか
def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        elif c == ')':
            score -= 1

        # 途中で 0 を下回るとダメ
        if score < 0:
            return False
    
    # 最後に 0 なら True、そうでなければ False
    return score == 0

# 入力
N = int(input())

# カッコ列を順に列挙していく
for bit in range((1 << N)):
    S = ""

    # 最上位の桁から順に見ていく
    for i in range(N - 1, -1, -1):
        if not (bit & (1 << i)):
            S += "("
        else:
            S += ")"

    # 整合していたら出力
    if isvalid(S):
        print(S)