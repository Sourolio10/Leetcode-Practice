def countWaysToMakeChangeUtil(arr, ind, T, dp):
    if ind == 0:
        return 1 if T % arr[0] == 0 else 0

    if dp[ind][T] != -1:
        return dp[ind][T]
        
    not_taken = countWaysToMakeChangeUtil(arr, ind-1, T, dp)
    
    taken = 0
    if arr[ind] <= T:
        taken = countWaysToMakeChangeUtil(arr, ind, T-arr[ind], dp)
        
    dp[ind][T] = not_taken + taken
    return dp[ind][T]


def countWaysToMakeChange(arr, n, T):
    dp = [[-1 for i in range(T+1)] for j in range(n)]
    return countWaysToMakeChangeUtil(arr, n-1, T, dp)

def main():
    arr = [1,2,3]
    target = 3
    n = len(arr)
    print("The total number of ways is", countWaysToMakeChange(arr, n, target))

if __name__ == "__main__":
    main()