def cheapflights(n, adj, src, dst, k):
    st = set()
    dist = [int(1e9)] * n

    st.add((0, src, 0))
    dist[src] = 0

    while st:
        it = next(iter(st))
        stops = it[0]
        node = it[1]
        cost = it[2]
        st.remove(it)

        if stops > k:
            continue
        for it in adj[node]:
            adjNode = it[0]
            edgW = it[1]

            if cost + edgW < dist[adjNode] and stops<=k:
                dist[adjNode] = cost + edgW
                st.add((stops+1, adjNode, dist[adjNode]))

    if dist[dst] == int(1e9):
        return -1
    return dist[dst]


n = 4
adj = [[] for _ in range(n)]
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
m= len(flights)
for i in range(m):
    adj[flights[i][0]].append((flights[i][1], flights[i][2]))
k=1
src = 0
dst = 3
print(cheapflights(n,adj, src, dst, k))
