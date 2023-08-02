from collections import deque
from typing import List

def topoSort(node: int, adj: List[List[int]], vis: List[int], st: deque) -> None:
    vis[node] = 1
    for i in range(len(adj[node])):
        v = adj[node][i][0]
        if vis[v] == 0:
            topoSort(v, adj, vis, st)
    st.append(node)

def shortestPath(N: int, M: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(N)]

    for i in range(M):
        u = edges[i][0]
        v = edges[i][1]
        wt = edges[i][2]
        adj[u].append([v, wt])

    vis = [0] * N
    st = deque()
    for i in range(N):
        if vis[i] == 0:
            topoSort(i, adj, vis, st)

    dist = [int(1e9)] * N
    dist[0] = 0
    while st:
        node = st.pop()

        for i in range(len(adj[node])):
            v = adj[node][i][0]
            wt = adj[node][i][1]

            if dist[node] + wt < dist[v]:
                dist[v] = wt + dist[node]

    for i in range(N):
        if dist[i] == 1e9:
            dist[i] = -1

    return dist

n = 6
m = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
res = shortestPath(n, m, edge)
for i in range(n):
    print(res[i], end=" ")
print()
