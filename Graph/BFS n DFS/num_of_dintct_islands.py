
from collections import deque
def bfs(graph, ro, co, vis):
    vis[ro][co] = 1
    n = len(graph)
    m = len(graph[0])

    q = deque()
    q.append((ro, co))
    
    while q:
        x = q.popleft()
        row = x[0]
        col = x[1]
       
        for vrow in range(-1,2):
            for vcol in range(-1,2):
                nrow = row + vrow
                ncol = col +  vcol

                if nrow >=0 and nrow <n and ncol >=0 and ncol <m and vis[nrow][ncol] ==0 and graph[nrow][ncol] == 1:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol))

def distinct(graph):
    
    n = len(graph)
    m = len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    c =0
    for row in range(n):
        for col in range(m):
            if vis[row][col] == 0 and graph[row][col] == 1:
                c+=1
                bfs(graph, row, col, vis)    

    return c

if __name__ == "__main__":
    n= int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    
    print(distinct(matrix))