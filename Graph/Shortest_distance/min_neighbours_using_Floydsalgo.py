
def findCity(n, m, edges, distanceThreshold):
    dist = [[int(1e9) for j in range(n)] for i in range(n)]
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] == int(1e9) or dist[k][i] == int(1e9):
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] +  dist[k][j])

    cntcity = n
    for city in range(n):
        cnt =0
        for adjcity in range(n):
            if dist[city][adjcity] <= distanceThreshold:
                cnt+=1
        if cnt <= cntcity:
            cntcity = cnt
            cityno =  city

    return cityno



n = 4
m = 4
edges = [(0, 1, 3), (1, 2, 1), (1, 3, 4), (2, 3, 1)]
distanceThreshold = 4


cityNo = findCity(n, m, edges, distanceThreshold)
print(f"The answer is node: {cityNo}")
