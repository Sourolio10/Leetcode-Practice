def sum1(arr):
    n = len(arr)
    dp = [-1 for _ in range(n)]
    dp[0] =  arr[0]
   
    
    for i in range(1, n):
        pick = arr[i]
        if dp[i]!=-1:
            return dp[i]
        if i> 1:
            pick = arr[i] + dp[i-2]
        nonPick = 0 + dp[i-1]
        dp[i] = max(pick, nonPick)

    return dp[n-1]

def main():
    arr = [1, 5, 1, 2, 6]
    arr1=[]
    arr2 =[]
    for i in range(len(arr)):
        if i!=0:
            arr1.append(arr[i])
        if i!= len(arr)-1:
            arr2.append(arr[i])
    print(arr1, arr2)
    print(max(sum1(arr1), sum1(arr2)))

if __name__ == '__main__':
    main()