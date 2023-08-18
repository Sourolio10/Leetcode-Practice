import sys
def solve(ind, height, dp):
    if ind <1:
        return ind
    elif dp[ind]!=-1:
        return dp[ind]
    jump2 = sys.maxsize
    jump1 = solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jump2 = solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jump1, jump2)
    return dp[ind]


if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(solve(n-1, height, dp))