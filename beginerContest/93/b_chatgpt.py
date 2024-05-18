def find_k_elements(A, B, K):
    # 範囲 [A, B] の全ての整数をリストにする代わりに、必要な部分だけ扱う
    small_k_elements = list(range(A, min(A + K, B + 1)))  # 小さい方から K 番目以内
    large_k_elements = list(range(max(B - K + 1, A), B + 1))  # 大きい方から K 番目以内
    
    # 小さい方と大きい方のリストを結合し、重複を排除してソートする
    result = sorted(set(small_k_elements + large_k_elements))
    
    return result

# テスト例
A,B,K = map(int,input().split())
ans = find_k_elements(A, B, K)  # 期待される出力: [5, 6, 7, 18, 19, 20]
for i in ans:
    print(i)
