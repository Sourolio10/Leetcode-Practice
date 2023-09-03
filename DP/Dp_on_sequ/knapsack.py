import sys
def knapsackUtil(wt, val, ind, W, dp):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    if dp[ind][W] != -1:
        return dp[ind][W]
    notTaken = 0 + knapsackUtil(wt, val, ind-1, W, dp)
    taken = -sys.maxsize
    if wt[ind] <= W:
        taken = val[ind] + knapsackUtil(wt, val, ind-1, W-wt[ind], dp)
    dp[ind][W] = max(notTaken, taken)
    return dp[ind][W]

def knapsack(wt, val, n, W):
    dp = [[-1 for j in range(W+1)] for i in range(n)]
    return knapsackUtil(wt, val, n-1, W, dp)

def main():
    wt = [1, 2, 4, 5]
    val = [5, 4, 8, 6]
    W = 5
    n = len(wt)
    print("The Maximum value of items, thief can steal is", knapsack(wt, val, n, W))

if __name__ == "__main__":
    main()