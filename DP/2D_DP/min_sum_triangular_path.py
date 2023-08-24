def minSumPathUtil(i, j, matrix, dp):
    n = len(matrix)
    if dp[i][j] != -1:
        return dp[i][j]
    if i == n-1:
        return matrix[i][j]
    down = matrix[i][j] + minSumPathUtil(i+1, j, matrix, dp)
    diagonal = matrix[i][j] + minSumPathUtil(i+1, j+1, matrix, dp)
    dp[i][j] = min(down, diagonal)
    return dp[i][j]

def minSumPath(n, m, matrix):
    dp = [[-1 for j in range(n)] for i in range(n)]
    return minSumPathUtil(0,0, matrix, dp)


def main():
    matrix = [[1], [2,3], [3,6,7], [8,9,6,10]]

    n = len(matrix)
    m = len(matrix[0])

    print(minSumPath(n, m, matrix))


if __name__ == '__main__':
    main()