import sys
def solve(ind, height, dp, k):
    if ind ==0:
        return 0
    elif dp[ind]!=-1:
        return dp[ind]
    
    mmSteps = sys.maxsize
    for j in range(1,k+1):
        if ind - j >= 0:
            jump1 = solve(ind-j, height, dp, k) + abs(height[ind] - height[ind-j])
    
            mmSteps = min(jump1, mmSteps)

    dp[ind] = mmSteps
    return dp[ind]


if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k=2
    dp = [-1 for i in range(n)]
    print(solve(n-1, height, dp,k))