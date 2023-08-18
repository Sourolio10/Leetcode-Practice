def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k=2
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for ind in range(1, n):
        mmSteps  = float('inf')
        for j in range(1, k+1):
            if ind - j >= 0:
                jump = dp[ind-j] + abs(height[ind]-height[ind-j])
                mmSteps = min(jump, mmSteps)

        dp[ind] = mmSteps
    print(dp[n-1])

if __name__ == "__main__":
    main()