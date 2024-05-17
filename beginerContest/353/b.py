N, K = map(int, input().split())  # N: グループの数, K: アトラクションの定員
A = list(map(int, input().split()))  # A: グループの人数のリスト

num_starts = 0  # アトラクションの出発回数
vacant_seats = K  # 空席数

for group_size in A:

    if group_size < vacant_seats:  # グループの人数が空席数を超えている場合

        num_starts += 1  # アトラクションを出発させる

        vacant_seats = K  # 空席数をKに戻す
        
    vacant_seats -= group_size  # 空席数を減らす

print(num_starts)
        
        
    