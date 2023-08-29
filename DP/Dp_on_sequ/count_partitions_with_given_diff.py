def solve(ind, arr, target, dp):
    if ind ==0:
        if target==0 and arr[ind]==0:
            return 2
        elif target==0 and arr[ind]==target:
            return 1
        return 0
    if dp[ind][target]!=-1:
        return dp[ind][target]
    notTaken = solve(ind-1, arr, target, dp)
    taken = 0
    if arr[ind]<= target:
        taken = solve(ind-1, arr, target - arr[ind], dp)
    dp[ind][target] = taken + notTaken
    return dp[ind][target]



if __name__ == "__main__":
    height = [0,0,1]
    target =1
    n = len(height)
    dp = [[-1 for j in range(target+1)] for i in range(n)]
    print(solve(n-1, height, target, dp))