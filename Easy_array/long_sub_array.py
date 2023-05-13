def getLongestSubarray(a,k,n):
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    k = int(input())
    n = len(arr)
    print(getLongestSubarray(arr,k,n))