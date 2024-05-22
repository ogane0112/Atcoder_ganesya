def kth_smallest_substring(s, k):
    substrings = set()

    # すべてのsubstringをセットに追加
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    
    # リストに変換してソート
    sorted_substrings = sorted(substrings)
    
    # K番目の要素を返す (0-indexedなのでK-1)
    return sorted_substrings[k - 1]

# 入力を受け取る
s = input("文字列sを入力してください: ")
k = int(input("Kを入力してください: "))

# K番目に小さいsubstringを出力
print("K番目に小さいsubstringは:", kth_smallest_substring(s, k))


