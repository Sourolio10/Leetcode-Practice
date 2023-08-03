

class Solution:
    def dfs(self, adj, s, st, vis):
        vis[s] = True
        for it in adj[s]:
            if not vis[it]:
                self.dfs(adj, it, st, vis) 
        
        st.append(s)
    # function to detect cycle in an undirected graph
    def isCycle(self, V, adj):
        vis = [False] * V
        
        st = []
        
        for i in range(V):
            if not vis[i]:
               self.dfs(adj, i, st, vis)
        ans =[]
        while st:
            ans.append(st.pop())
        return ans
    

def main():
    adj = [[] for _ in range(6)]
    adj[2].append(3)
    adj[3].append(1)
    adj[4].append(0)
    adj[4].append(1)
    adj[5].append(0)
    adj[5].append(2)


    obj = Solution()
    ans = obj.isCycle(6, adj)
    print(ans)

if __name__ == "__main__":
    main()
