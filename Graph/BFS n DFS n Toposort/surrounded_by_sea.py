def dfs(row, col, vrow, vcol, graph, vis,n,m):
    vis[row][col] = 1

    for i in range(4):
        nrow = row + vrow[i]
        ncol = col + vcol[i]

        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol] == 0 and graph[nrow][ncol] == 1:
            dfs(nrow, ncol, vrow, vcol, graph, vis,n,m)


def surrounded(graph):

    n = len(graph)
    m = len(graph[0])

    vis = [[0 for _ in range(m)] for _ in range(n)]

    vrow = [-1,0,1,0]
    vcol = [0,1,0,-1]

    for j in range(m):
        if vis[0][j] == 0 and graph[0][j] == 1:
            dfs(0, j, vrow, vcol, graph, vis,n,m)

        if vis[n-1][j] == 0 and graph[n-1][j] == 1:
            dfs(n-1, j, vrow, vcol, graph, vis,n,m)

    for i in range(n):
        if vis[i][0] == 0 and graph[i][0] == 1:
            dfs(i, 0, vrow, vcol, graph, vis,n,m)

        if vis[i][m-1] == 0 and graph[i][m-1] == 1:
            dfs(i, m-1, vrow, vcol, graph, vis,n,m)
    c=0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and graph[i][j] == 1:
                c+=1
    
    print(c)


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

    
    surrounded(matrix)