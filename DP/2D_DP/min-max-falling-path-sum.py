import sys
def getMaxUtil(i, j, m, matrix, dp):
    if j < 0 or j >= m:
        return -int(1e9)
    if i == 0:
        return matrix[0][j]
    if dp[i][j] != -1:
        return dp[i][j]
    up = matrix[i][j] + getMaxUtil(i-1, j, m, matrix, dp)
    leftDiagonal = matrix[i][j] + getMaxUtil(i-1, j-1, m, matrix, dp)
    rightDiagonal = matrix[i][j] + getMaxUtil(i-1, j+1, m, matrix, dp)
    dp[i][j] = max(up, max(leftDiagonal, rightDiagonal))
    return dp[i][j]

def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1 for j in range(m)] for i in range(n)]
    maxi = -sys.maxsize
    for j in range(m):
        ans = getMaxUtil(n-1, j, m, matrix, dp)
        maxi = max(maxi, ans)
    return maxi

def main():
    matrix = [[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
    print(getMaxPathSum(matrix))

if __name__ == "__main__":
    main()