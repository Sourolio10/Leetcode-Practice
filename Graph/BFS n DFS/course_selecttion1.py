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
    n = int(input())
    m = int(input())

    # Initialize an empty matrix
    matrix = []
    for i in range(m):
        row = []
        for j in range(2):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    adj = [[] for _ in range(n)]
    for i in range(m):
        adj[matrix[i][1]].append(matrix[i][0])



    obj = Solution()
    ans = obj.Topo(n, adj)
    if len(ans) == n:
        print(ans)
    else:
        print([])

if __name__ == "__main__":
    main()
