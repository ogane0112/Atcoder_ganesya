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

# 入力例
N = 6
cards = [(32, 101, 1), (65, 78, 2), (2, 29, 3), (46, 55, 4), (103, 130, 5), (52, 40, 6)]

# カードをフィルタリング
result_indices = filter_cards(cards)

# 結果を出力
print(len(result_indices))
print(' '.join(map(str, result_indices)))
