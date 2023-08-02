from collections import deque
class Solution:
    
    def dist(self, edge, n, m, src):
       
        dist = [[] for _ in range(n)]
        for i in range(n):
            dist[i] = int(1e9)

        adj = [[] for _ in range(n)]
        for i in range(m):
            adj[edge[i][0]].append(edge[i][1])
            adj[edge[i][1]].append(edge[i][0])
        q = deque()
        
        q.append(src)
        dist[src] =0


        while q:
            x = q.popleft()
            
            for it in adj[x]:
                if (dist[it] > (dist[x] +1)):
                    dist[it] = dist[x] +1
                    q.append(it)

        return dist

def main():
    n=9
    m=10
    edge = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]


    obj = Solution()
    ans = obj.dist(edge, n, m, 0)
    print(ans)

if __name__ == "__main__":
    main()
