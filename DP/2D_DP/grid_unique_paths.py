def countWaysUtil(i, j, dp):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = countWaysUtil(i - 1, j, dp)
    left = countWaysUtil(i, j - 1, dp)
    dp[i][j] = up + left
    return dp[i][j]

def countWays(m, n):
    dp = [[-1 for j in range(n)] for i in range(m)]
    return countWaysUtil(m - 1, n - 1, dp)

def main():
    m = 3
    n = 2
    print(countWays(m, n))

if __name__ == '__main__':
    main()