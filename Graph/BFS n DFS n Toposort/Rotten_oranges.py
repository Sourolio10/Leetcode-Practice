from collections import deque
def rotten(graph):
    vis, q = set(), deque()

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                vis.add((i,j))
            elif graph[i][j] == 2:
                q.append((i,j))
    res=0
    while vis and q:
        for _ in range(len(q)):
            i,j = q.popleft()

            for pos in((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                if pos in vis:
                    vis.remove(pos)
                    q.append(pos)
        res+=1
    print(res)

if __name__ == "__main__":
    n= int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    
    rotten(matrix)