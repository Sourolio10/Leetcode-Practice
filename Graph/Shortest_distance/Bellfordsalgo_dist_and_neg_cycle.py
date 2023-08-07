
def dist(V, src, edges):
    
    dist = [int(1e9)] * V
    dist[src] = 0

    for i in range(V-1):
        for u, v, edW in edges:
            if dist[u] != 1e9 and dist[v] > dist[u] + edW:
                dist[v] = dist[u] + edW

    for i in range(V-1):
        for u, v, edW in edges:
            if dist[u] != 1e9 and dist[v] > dist[u] + edW:
                temp = -1
                return temp
            
    return dist

edges = [(3, 2, 6), (5, 3, 1), (0, 1, 5), (1, 5, -3), (1, 2, -2), (3, 4, -2), (2, 4, 3)]

V = 6
src =0
 

print(dist(V, src, edges))