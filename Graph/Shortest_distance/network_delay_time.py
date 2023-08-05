from queue import PriorityQueue
def dijkstra(n, adj, src):
    q = PriorityQueue()
    dist = {i:float('inf') for i in range(1, n+1)}

    dist[src] = 0
    q.put((0,src))

    while not q.empty():
        time, node = q.get()
        for currnode, delay in adj[node]:

            if dist[currnode] > time + delay:
                dist[currnode] = time + delay
                q.put((dist[currnode], currnode))
    ans = max(dist.values())
    return ans if ans != int(1e9) else -1


times = [[1,2,1]]
adj = [[] for _ in range(3)]
for u, v, c in times:
    adj[u].append((v, c))
print(adj)
src = 1
print(dijkstra(2, adj, src))