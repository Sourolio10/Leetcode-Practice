def minimumElementsUtil(arr, ind, T, dp):
    if ind == 0:
        if T%arr[0] == 0:
            return T//arr[0]
        else:
            return int(1e9)
    if dp[ind][T] != -1:
        return dp[ind][T]
    notTaken = 0 + minimumElementsUtil(arr, ind-1, T, dp)
    taken = int(1e9)
    if arr[ind] <= T:
        taken = 1 + minimumElementsUtil(arr, ind, T-arr[ind], dp)
    dp[ind][T] = min(notTaken, taken)
    return dp[ind][T]

def minimumElements(arr, T):
    n = len(arr)
    dp = [[-1 for j in range(T+1)] for i in range(n)]
    ans = minimumElementsUtil(arr, n-1, T, dp)
    if ans >= int(1e9):
        return -1
    return ans

def main():
    arr = [1, 2, 3]
    T = 7
    print("The minimum number of coins required to form the target sum is", minimumElements(arr, T))

if __name__ == '__main__':
    main()