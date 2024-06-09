from collections import defaultdict
import bisect
i_list = []
d  =defaultdict(int)
m  = int(int(input()))
for i in range(m):
    a,b = map(int,input().split()) 
    c = i + 1
    i_list.append((a,b,c))
def filter_cards(cards):
    # カードを強さでソート（インデックスも含む）
    cards.sort(key=lambda card: card[0])
    
    # 残すべきカードのインデックスを保持するリスト
    filtered_indices = []
    
    # 現在の最大コスト
    max_cost = float('inf')
    
    # 強さの順でソートされたカードを逆順に走査
    for strength, cost, index in reversed(cards):
        if cost < max_cost:
            filtered_indices.append(index)
            max_cost = cost
    
    # インデックスを昇順にソート
    filtered_indices.sort()
    
    return filtered_indices

# 2番目の要素でソート
sorted_data = sorted(i_list, key=lambda x: x[0])
result_indices = filter_cards(sorted_data)
print(len(result_indices))
print(' '.join(map(str, result_indices)))
