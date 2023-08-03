def provinces(graph):
    vis = [False]*len(graph)
    def DFS(i):
        for j in range(len(graph)):
            if graph[i][j] and not vis[j]:
                vis[j] = True
                DFS(j)


    ans =0
    for i in range(len(graph)):
        if not vis[i]:
            DFS(i)
            ans+=1
    print(ans)

if __name__ == "__main__":
    n= int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    
    provinces(matrix)