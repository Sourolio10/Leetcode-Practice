def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for ind in range(1, n):
        jumpTwo = float('inf')
        jumpOne = dp[ind-1] + abs(height[ind]-height[ind-1])
        if ind > 1:
            jumpTwo = dp[ind-2] + abs(height[ind]-height[ind-2])
        dp[ind] = min(jumpOne, jumpTwo)
    print(dp[n-1])

if __name__ == "__main__":
    main()