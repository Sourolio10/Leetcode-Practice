from collections import deque
class Solution:
    
    def Topo(self, V, adj):
       
        st = []
        indegree = [0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)


        while q:
            x = q.popleft()
            st.append(x)
            for it in adj[x]:
                indegree[it]-=1
                if indegree[it] == 0:
                    q.append(it)

        return st

def main():
    adj = [[] for _ in range(6)]
    adj[1].append(2)
    adj[4].append(1)
    adj[2].append(4)
    adj[3].append(4)
    adj[5].append(2)
    adj[1].append(3)



    obj = Solution()
    ans = obj.Topo(6, adj)
    if len(ans) == 6:
        print('DAG')
    else:
        print('Cycle is present')

if __name__ == "__main__":
    main()
