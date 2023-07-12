from collections import deque

def dfs(graph, v, visited):
    stack = deque()
    stack.append(v)
    while stack:
        v = stack.pop()
        visited[v] = True
        adj_list = graph[v]
        for i in reversed(range(len(adj_list))):
            u = adj_list[i]
            if not visited[u]:
                stack.append(u)

n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
roads = []

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        roads.append(i)
        dfs(adj_list, i, visited)

print(len(roads) - 1)
for e in range(len(roads) - 1):
    print(roads[e], roads[e+1])
