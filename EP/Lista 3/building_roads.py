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

# from collections import deque
 
# def generate_graph(edges, n): 
#     adj_list = [[] for _ in range(0, n+1)]
#     for (src, dest) in edges:
#         adj_list[dest].append(src)
#     return adj_list

# def find_route(graph, src, dest):
#     n = len(graph) +1
#     discovered = [False] * (n+1)
#     q = deque()
#     discovered[src] = True
#     q.append(src)
#     while q:
#         v = q.popleft()
#         if v == dest:
#             return True
#         for u in graph[v]:
#             if not discovered[u]:
#                 discovered[u] = True
#                 q.append(u)
#     return False

# n, m =  map(int, input().split())
# roads = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     roads.append((a, b))
# graph = generate_graph(roads, n)
# e, i = n, n
# out = []
# while e > 0 and i > 0:
#     (src, dest) = (e, i)
#     if find_route(graph, src, dest):
#         i-=1
#         if(i < n-1):
#             e -= 1
#     else:
#         roads.append((dest, src))
#         out.append([dest, src])
#         graph = generate_graph(roads, n)

# print(len(out))
# for e in out:
#     print(e[0], e[1])