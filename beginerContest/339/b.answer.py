h, w, n = map(int, input().split())

# 初期位置と方向を設定
x, y = 0, 0  # (1, 1)に相当する
direction = 0  # 上を向いている(0: 上, 1: 右, 2: 下, 3: 左)

# グリッドを初期化
grid = [['.' for _ in range(w)] for _ in range(h)]

# 移動関数
def move(x, y, direction):
    if grid[x][y] == '.':  # 白マスの場合
        grid[x][y] = '#'  # 黒に塗る
        direction = (direction + 1) % 4  # 時計回りに90度回転
    else:  # 黒マスの場合
        grid[x][y] = '.'  # 白に塗る
        direction = (direction - 1) % 4  # 反時計回りに90度回転

    # 新しい位置を計算
    if direction == 0:  # 上
        x = (x - 1) % h
    elif direction == 1:  # 右
        y = (y + 1) % w
    elif direction == 2:  # 下
        x = (x + 1) % h
    else:  # 左
        y = (y - 1) % w

    return x, y, direction

# N回操作を実行
for _ in range(n):
    x, y, direction = move(x, y, direction)

# 結果を出力
for row in grid:
    print(''.join(row))