import heapq

def dijkstra(adj, origin):
    n = len(adj)
    distance = [float('inf')] * n
    distance[origin] = 0
    heap = [(0, origin)]

    while heap:
        dist, u = heapq.heappop(heap)
        if dist > distance[u]:
            continue
        for v, w in adj[u]:
            old_dist = distance[v]
            new_dist = distance[u] + w
            if old_dist > new_dist:
                distance[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    return distance

n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))

res = dijkstra(adj_list, 1)
for i in range(1, len(res)):
    print(res[i], end=' ')