from collections import deque

class Solution:
    def checkForCycle(self, adj, s, vis, parent):
        q = deque()  # BFS
        q.append((s, -1))
        vis[s] = True
        
        # until the queue is empty
        while q:
            # source node and its parent node
            node, par = q.popleft()
            
            # go to all the adjacent nodes
            for it in adj[node]:
                if not vis[it]:
                    q.append((it, node))
                    vis[it] = True
                # if adjacent node is visited and is not its own parent node
                elif par != it:
                    return True
        
        return False

    # function to detect cycle in an undirected graph
    def isCycle(self, V, adj):
        vis = [False] * V
        parent = [-1] * V
        
        for i in range(V):
            if not vis[i]:
                if self.checkForCycle(adj, i, vis, parent):
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
