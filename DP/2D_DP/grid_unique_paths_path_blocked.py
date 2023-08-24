def countWaysUtil(i, j, maze, dp):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0 or maze[i][j] == -1:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = countWaysUtil(i - 1, j, maze, dp)
    left = countWaysUtil(i, j - 1, maze, dp)
    dp[i][j] = up + left
    return dp[i][j]

def countWays(m, n, maze):
    dp = [[-1 for j in range(n)] for i in range(m)]
    return countWaysUtil(m - 1, n - 1, maze, dp)

def main():
    maze = [[0,0,0], [0,-1,0], [0,0,0]]
    m = 3
    n = 3
    print(countWays(m, n, maze))

if __name__ == '__main__':
    main()