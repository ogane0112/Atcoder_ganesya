def count_connected_components(coords, connected_pairs):
    # 隣接リストの作成
    graph = {coord: [] for coord in coords}
    for pairs in connected_pairs:
        for pair in pairs:
            graph.setdefault(pair[0], [])
            graph.setdefault(pair[1], [])
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    # 未訪問の頂点を管理するためのセット
    unvisited = set(coords)
    connected_components_count = 0

    while unvisited:
        # 未訪問の頂点からDFSを開始し、連結成分を見つける
        start_node = unvisited.pop()
        dfs(start_node, set())
        connected_components_count += 1

    return connected_components_count

# テスト
coords = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6), (4, 1), (4, 3), (5, 3)]
connected_pairs = [[(1, 3)], [(1, 2), (2, 4)], [(1, 3), (3, 5)], [(2, 4), (3, 6)], [(3, 5)], [], [(5, 3)], [(4, 3)]]
print(count_connected_components(coords, connected_pairs))  # Output: 3

