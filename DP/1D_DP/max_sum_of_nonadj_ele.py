def solveUtil(ind, arr, dp):
    if dp[ind]!=-1:
        return dp[ind]
    if ind==0:
        return arr[ind]
    if ind<0:
        return 0
    pick = arr[ind] + solveUtil(ind-2, arr, dp)
    nonPick = 0 + solveUtil(ind-1, arr, dp)
    dp[ind] = max(pick, nonPick)
    return dp[ind]

def solve(n, arr):
    dp = [-1 for i in range(n)]
    return solveUtil(n-1, arr, dp)

def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    print(solve(n, arr))

if __name__ == '__main__':
    main()