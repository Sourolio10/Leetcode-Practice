from collections import deque

class Solution:
    def dfs(self, node, col, color, adj):
        color[node] = col
        for it in adj[node]:
            if color[it] == -1:
                if self.dfs(it, 1 - color[node], color, adj) == False:
                    return False
            elif color[it] == col:
                return False
        return True

    # function to detect cycle in an undirected graph
    def isbipirite(self, V, adj):
  
        color = [-1] * V
        
        for i in range(V):
            if color[i] == -1:
                if not self.dfs(i, 0, color, adj):
                    return False
        
        return True

def main():
    adj = [[] for _ in range(4)]
    adj[0].append(2)
    adj[2].append(0)
    adj[0].append(3)
    adj[3].append(0)
    adj[1].append(3)
    adj[3].append(1)
    adj[2].append(3)
    adj[3].append(2)

    obj = Solution()
    ans = obj.isbipirite(4, adj)
    if ans:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
