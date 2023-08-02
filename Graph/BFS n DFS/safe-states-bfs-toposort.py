from collections import deque
class Solution:
    
    def Topo(self, V, adj):
        adjrev = [[] for _ in range(12)]
        st = []
        indegree = [0]*V
        for i in range(V):
            for it in adj[i]:
                adjrev[it].append(i)
                indegree[i]+=1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)


        while q:
            x = q.popleft()
            st.append(x)
            for it in adjrev[x]:
                indegree[it]-=1
                if indegree[it] == 0:
                    q.append(it)

        return sorted(st)

def main():
    adj = [[] for _ in range(12)]
    adj[0].append(1)
    adj[1].append(2)
    adj[2].append(3)
    adj[2].append(4)
    adj[3].append(4)
    adj[3].append(5)
    adj[4].append(6)
    adj[5].append(6)
    adj[6].append(7)
    adj[8].append(1)
    adj[8].append(9)
    adj[9].append(10)
    adj[10].append(8)
    adj[11].append(9)



    obj = Solution()
    ans = obj.Topo(12, adj)
    print(ans)

if __name__ == "__main__":
    main()
