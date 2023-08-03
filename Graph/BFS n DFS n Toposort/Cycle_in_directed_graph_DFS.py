from collections import deque

class Solution:
    def dfs(self, adj, s, vis, pathvis):
        vis[s] = True
        pathvis[s] = 1
        for it in adj[s]:
            if not vis[it]:
                if self.dfs(adj, it, vis, pathvis) == True:
                    return True
            elif pathvis[it] == 1:
                return True
        return False
    # function to detect cycle in an undirected graph
    def isCycle(self, V, adj):
        vis = [False] * V
        pathvis = [0]* V
        
        for i in range(V):
            if not vis[i]:
                if self.dfs(adj, i, vis, pathvis):
                    return True
        
        return False

def main():
    adj = [[] for _ in range(11)]
    adj[1].append(2)
    adj[2].append(3)
    adj[3].append(4)
    adj[3].append(7)
    adj[4].append(5)
    adj[5].append(6)
    adj[7].append(5)
    adj[8].append(9)
    adj[9].append(10)
    adj[10].append(8)

    obj = Solution()
    ans = obj.isCycle(11, adj)
    if ans:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
