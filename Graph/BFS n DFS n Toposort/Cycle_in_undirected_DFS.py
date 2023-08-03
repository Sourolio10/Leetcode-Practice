from collections import deque

class Solution:
    def dfs(self, adj, s, vis, parent):
        vis[s] = True
        for it in adj[s]:
            if not vis[it]:
                if self.dfs(adj, it, vis, s) == True:
                    return True
            elif parent!= it:
                return True
        return False
    # function to detect cycle in an undirected graph
    def isCycle(self, V, adj):
        vis = [False] * V
        
        
        for i in range(V):
            if not vis[i]:
                if self.dfs(adj, i, vis, -1):
                    return True
        
        return False

def main():
    adj = [[] for _ in range(4)]
    adj[1].append(2)
    adj[2].append(1)
    adj[2].append(3)
    adj[3].append(2)

    obj = Solution()
    ans = obj.isCycle(4, adj)
    if ans:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
