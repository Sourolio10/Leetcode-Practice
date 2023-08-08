from queue import PriorityQueue
def spanningTree(V, adj):
    q = PriorityQueue()
    q.put((int(0), int(0)))

    vis = [0]*V
    sum=0

    while not q.empty():
        wt, node = q.get()

        if vis[node] == 1:
            continue

        vis[node] = 1
        sum+=wt

        for adjNode, edW in adj[node]:
            if vis[adjNode] == 0:
                q.put((edW, adjNode))


    return sum



V = 5
adj = [[] for _ in range(V)]
edges = [(0, 1, 2), (0, 2, 1), (1, 2, 1), (2, 3, 2), (3, 4, 1), (4, 2, 2)]

for i in range(6):
    u, v, w = edges[i]
    adj[u].append([v, w])
    adj[v].append([u, w])


sum = spanningTree(V, adj)
print(f"The sum of all the edge weights: {sum}")
