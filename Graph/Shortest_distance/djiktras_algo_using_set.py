from typing import List

def dijkstra(V: int, adj: List[List[int]], S: int) -> List[int]:
    st = set()
    dist = [int(1e9)] * V

    st.add((0, S))
    dist[S] = 0

    while st:
        it = next(iter(st))
        node = it[1]
        dis = it[0]
        st.remove(it)

        for it in adj[node]:
            adjNode = it[0]
            edgW = it[1]

            if dis + edgW < dist[adjNode]:
                if dist[adjNode] != 1e9:
                    st.remove((dist[adjNode], adjNode))

                dist[adjNode] = dis + edgW
                st.add((dist[adjNode], adjNode))

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
