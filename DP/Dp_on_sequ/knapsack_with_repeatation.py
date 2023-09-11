import sys
def knapsackUtil(wt, val, ind, W, dp):
    if ind == 0:
        return (W // wt[0]) * val[0]

    if dp[ind][W] != -1:
        return dp[ind][W]

    notTaken = knapsackUtil(wt, val, ind - 1, W, dp)

    taken = -sys.maxsize
    if wt[ind] <= W:
        taken = val[ind] + knapsackUtil(wt, val, ind, W - wt[ind], dp)

    dp[ind][W] = max(notTaken, taken)
    return dp[ind][W]

def unboundedKnapsack(n, W, val, wt):
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    return knapsackUtil(wt, val, n - 1, W, dp)

def main():
    wt = [2, 4, 6]
    val = [5, 11, 13]
    W = 10
    n = len(wt)

    print("The Maximum value of items, thief can steal is", unboundedKnapsack(n, W, val, wt))

if __name__ == "__main__":
    main()