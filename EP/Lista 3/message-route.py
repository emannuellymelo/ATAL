from collections import deque
def bfs(n, routes):
    g = [[] for _ in range(n+1)]
    for a, b in routes:
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n+1)
    pi = [-1] * (n+1)
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        current_node = queue.popleft()
        if current_node == n: break
        for adj in g[current_node]:
            if not visited[adj]:
                visited[adj] = True
                pi[adj] = current_node
                queue.append(adj)

    if not visited[n]:
        return "IMPOSSIBLE"

    path = []
    current_node = n
    while(current_node != -1):
        path.append(current_node)
        current_node = pi[current_node]

    path.reverse()
    return path

n, m = map(int, input().split())
routes = []
for _ in range(m):
    a, b = map(int, input().split())
    routes.append((a, b))

res = bfs(n, routes)
if(res != "IMPOSSIBLE"):
    print(len(res))
    print(*res)
else:
    print(res)
