def minSumPathUtil(i, j, matrix, dp):
    
    if i == 0 and j == 0:
        return matrix[0][0]
    if i < 0 or j < 0:
        return int(1e9)
    if dp[i][j] != -1:
        return dp[i][j]
    up = matrix[i][j] + minSumPathUtil(i-1, j, matrix, dp)
    left = matrix[i][j] + minSumPathUtil(i, j-1, matrix, dp)
    dp[i][j] = min(up, left)
    return dp[i][j]

def minSumPath(n, m, matrix):
    dp = [[-1 for j in range(m)] for i in range(n)]
    return minSumPathUtil(n-1, m-1, matrix, dp)


def main():
    matrix = [[5, 9, 6],
              [11, 5, 2]]

    n = len(matrix)
    m = len(matrix[0])

    print(minSumPath(n, m, matrix))


if __name__ == '__main__':
    main()