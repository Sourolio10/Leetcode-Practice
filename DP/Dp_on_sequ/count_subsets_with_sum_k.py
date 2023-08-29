def solve(ind, arr, target, dp):
    if target==0:
        return 1
    if ind ==0:
        return arr[ind] == target
    if dp[ind][target]!=-1:
        return dp[ind][target]
    notTaken = solve(ind-1, arr, target, dp)
    taken = 0
    if arr[ind]<= target:
        taken = solve(ind-1, arr, target - arr[ind], dp)
    dp[ind][target] = taken + notTaken
    return dp[ind][target]



if __name__ == "__main__":
    height = [1,2,3,4]
    target =8
    n = len(height)
    dp = [[-1 for j in range(target+1)] for i in range(n)]
    print(solve(n-1, height, target, dp))