def color(graph, sr, sc, color1):
    vis = set()
    def DFS(row, col):
        if row <0 or col<0 or row== len(graph) or col == len(graph[0]):
            return
        if graph[row][col]!=0 and (row,col) not in vis:
            vis.add((row,col))
        
            
            graph[row][col] = color1

            DFS(row-1, col)
            DFS(row, col-1)
            DFS(row+1, col)
            DFS(row, col+1)

        return

    DFS(sr, sc)
    print(graph)

if __name__ == "__main__":
    n= int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    sr = int(input())
    sc = int(input())
    
    color1 = int(input())
    
    color(matrix, sr, sc, color1)