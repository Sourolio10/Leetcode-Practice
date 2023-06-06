def binary(arr, n):
    low = 0
    high =n-1
    min1 = 9999
    while(low<=high):
        if arr[low]< arr[high]:
            min1 = min(min1, arr[low])
            return min1
            break
        mid = (low+high)//2
        if arr[low]<= arr[mid]:
            min1 = min(min1, arr[low])
            low= mid+1
        else:
            min1 = min(min1, arr[mid])
            high=mid-1
    return min1
# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(binary(arr, n))