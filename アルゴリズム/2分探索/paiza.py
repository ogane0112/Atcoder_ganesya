def max_avg_subarray(nums, k):
    n = len(nums)
    left, right = 0, n - k  # 探索範囲の初期化
    
    # 最初のk個の要素の合計を計算
    curr_sum = sum(nums[:k])
    max_sum = curr_sum  # 最大の合計を初期化
    max_start_idx = 0  # 最大の平均値を持つ区間の開始インデックスを初期化
    max_count = 1  # 最大の平均値の区間の個数を初期化

    while left <= right:
        # 現在の区間の平均値を計算
        curr_avg = curr_sum / k

        # 最大の平均値を更新
        if curr_avg > max_sum / k:
            max_sum = curr_sum
            max_start_idx = left  # 最大の平均値を持つ区間の開始インデックスを更新
            max_count = 1  # 最大の平均値の区間の個数を1にリセット
        elif curr_avg == max_sum / k:
            max_count += 1  # 最大の平均値の区間の個数を増やす

        # 次の区間に移動
        if left < right:
            curr_sum = curr_sum - nums[left] + nums[left + k]
        left += 1

    # 最後の区間が最大の平均値の場合、個数を減らす
    if left == n:
        max_count -= 1

    max_avg = max_sum / k
    return max_start_idx, max_avg, max_count

# 使用例
nums = [6, 2, 0, 7, 1, 3, 5, 3, 2, 6]
k = 3
start, max_avg, count = max_avg_subarray(nums, k)
print(f"最大の平均値 {max_avg} は、インデックス {start} から始まる長さ {k} の区間にあり、その個数は {count} 個です。")