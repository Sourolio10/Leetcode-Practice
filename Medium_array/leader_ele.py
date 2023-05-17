def printLeaders(arr, n):
    ans = []
  
    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(printLeaders(arr, n))