from queue import PriorityQueue
def dijkstra(n, adj, src):
    q = PriorityQueue()
    dist = [int(1e9)] * n

    dist[src] = 0
    q.put((0,src))

    while not q.empty():
        node = q.queue[0][1]
        weight = q.queue[0][1]
        q.get()
        for it in adj[node]:
            N = it[0]
            W = it[1]

            if dist[N] > weight + W:
                dist[N] = weight + W
                q.put((dist[N],N))

    return dist




V = 3
E = 3
S = 2
adj = [[], [], []]
edges = []
v1 = [1, 1]
v2 = [2, 6]
v3 = [2, 3]
v4 = [0, 1]
v5 = [1, 3]
v6 = [0, 6]

adj[0].append(v1)
adj[0].append(v2)
adj[1].append(v3)
adj[1].append(v4)
adj[2].append(v5)
adj[2].append(v6)

res = dijkstra(V, adj, S)

for i in range(V):
    print(res[i], end=" ")
print()