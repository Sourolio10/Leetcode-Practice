from queue import PriorityQueue
def no_of_ways(n, adj):
    q = PriorityQueue()
    dist = [int(1e9)] * n
    ways = [0 for _ in range(n)]
    dist[0] = 0
    ways[0] = 1
    q.put((0,0))
    mod = (int)(1e9 + 7)
    while not q.empty():
        dis, node = q.get()
        for adjnode, edW in adj[node]:
            
            if dist[adjnode] > dis + edW:
                dist[adjnode] = dis + edW
                q.put((dist[adjnode], adjnode))
                ways[adjnode] =  ways[node]

            elif dist[adjnode] == dis + edW:
                ways[adjnode] = (ways[adjnode] + ways[node]) % mod


    
    return ways[n-1] % mod


roads = [(0, 6, 7), (0, 1, 2), (1, 2, 3), (1, 3, 3), (6, 3, 3), (3, 5, 1), (6, 5, 1), (2, 5, 1), (0, 4, 5), (4, 6, 2)]
n=7
adj = [[] for _ in range(n)]
m = len(roads)
for i in range(m):
    adj[roads[i][0]].append((roads[i][1], roads[i][2]))
    adj[roads[i][1]].append((roads[i][0], roads[i][2]))
print(no_of_ways(n, adj))