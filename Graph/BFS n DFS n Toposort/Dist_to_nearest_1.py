
from collections import deque
def dis(graph):
    n = len(graph)
    m = len(graph[0])

    vis = [[0 for _ in range(m)] for _ in range(n)]
    dist = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i,j,0))
                vis[i][j]=1
    
    vrow = [-1,0,1,0]
    vcol = [0,1,0,-1]

    while q:
        x = q.popleft()
        row = x[0]
        col = x[1]
        steps = x[2]
        dist[row][col] = steps

        for i in range(4):
            nrow = row + vrow[i]
            ncol = col +  vcol[i]

            if nrow >=0 and nrow <n and ncol >=0 and ncol <m and vis[nrow][ncol] ==0:
                vis[nrow][ncol] = 1
                q.append((nrow, ncol, steps+1))
    
    return dist


if __name__ == "__main__":
    n= int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    
    print(dis(matrix))