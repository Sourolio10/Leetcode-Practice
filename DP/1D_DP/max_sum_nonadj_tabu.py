def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    dp = [-1 for _ in range(n)]
    dp[0] =  arr[0]
    for i in range(1, n):
        if dp[i]!=-1:
            return dp[i]
        pick = arr[i] + dp[i-2]
        nonPick = 0 + dp[i-1]
        dp[i] = max(pick, nonPick)

    print(dp[n-1])

if __name__ == '__main__':
    main()