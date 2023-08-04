from queue import PriorityQueue
from typing import List, Tuple


def min_effort(maze):
    row = len(maze)
    col = len(maze[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = PriorityQueue()
    queue.put((0,0,0))
    distance = [[float('inf') for i in range(col)] for j in range(row)]
    
    while queue:
        diff = queue.queue[0][1]
        r = queue.queue[0][1]
        c = queue.queue[0][1]
        queue.get()
        if r == row -1 and c == col - 1:
            return diff
        for i in range(4):
            rr, cc = r + dx[i], c + dy[i]
            if (rr >= 0) and (rr < row) and (cc >= 0) and (cc < col):
                maxdiff = max((abs(maze[r][c] - maze[rr][cc]), diff))

                if distance[rr][cc] > maxdiff:
                    distance[rr][cc] = maxdiff
                    queue.put((maxdiff, rr, cc))


maze = [[1, 2, 2],
        [3, 8, 2],
        [5, 3, 5]]

print(min_effort(maze))
