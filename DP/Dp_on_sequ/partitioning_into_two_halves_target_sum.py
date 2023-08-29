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
    height = [1,2,3,4,5]
    if sum(height) %2 ==1:
        print(False)
    else:
        target = sum(height) //2    
        n = len(height)
        dp = [[-1 for j in range(target+1)] for i in range(n)]
        print(solve(n-1, height, target, dp))