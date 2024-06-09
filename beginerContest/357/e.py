def dfs(graph, node, visited):
    if visited[node]:
        return 0
    visited[node] = True
    count = 1  # 自分自身をカウント
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    return count

def count_reachable_nodes(n, edges):
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    reachable_count = []
    for i in range(n):
        visited = [False] * n
        count = dfs(graph, i, visited)
        reachable_count.append(count)
    
    return reachable_count


n = int(input())

a = list(map(int,input().split()))
edge = []
for i in range(n):
    edge.append((i,a[i]-1))

ans = count_reachable_nodes(n, edge)

print(sum(ans))