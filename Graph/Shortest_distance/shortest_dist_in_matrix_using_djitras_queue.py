from collections import deque
from typing import List, Tuple


def shortest_distance(maze: List[List[int]], src: Tuple[int, int], dest: Tuple[int, int]) -> int:
    row = len(maze)
    col = len(maze[0])
    visited = [[False for i in range(col)] for j in range(row)]
    distance = [[float('inf') for i in range(col)] for j in range(row)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque()
    queue.append(src)
    visited[src[0]][src[1]] = True
    distance[src[0]][src[1]] = 0
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            rr, cc = r + dx[i], c + dy[i]
            if (rr >= 0) and (rr < row) and (cc >= 0) and (cc < col) and maze[rr][cc] == 1:
                if not visited[rr][cc]:
                    visited[rr][cc] = True
                    distance[rr][cc] = distance[r][c] + 1
                    queue.append((rr, cc))
                else:
                    if distance[r][c] + 1 < distance[rr][cc]:
                        distance[rr][cc] = distance[r][c] + 1
                        queue.append((rr, cc))
    
    if distance[dest[0]][dest[1]] != float('inf'):
        return distance[dest[0]][dest[1]]
    else:
        return -1

maze = [[1, 0, 1, 1],
        [1, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 1]]
src = (3, 0)
dest = (0, 3)
print(shortest_distance(maze, src, dest))
