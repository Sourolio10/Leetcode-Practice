def solve(ind, arr, target, dp):
    if target==0:
        return True
    if ind ==0:
        return arr[ind]==target
    if dp[ind][target]!=-1:
        return dp[ind][target]
    notTaken = solve(ind-1, arr, target, dp)
    taken = False
    if arr[ind]<= target:
        taken = solve(ind-1, arr, target - arr[ind], dp)
    dp[ind][target] = taken or notTaken
    return dp[ind][target]



if __name__ == "__main__":
    arr = [1,2,3,4]
    n = len(arr)
    totSum = sum(arr)
    dp = [[-1 for i in range(totSum + 1)] for j in range(n)]

    for i in range(totSum + 1):
        dummy = solve(n - 1, arr, i, dp)

    mini = int(1e9)
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    print(mini)