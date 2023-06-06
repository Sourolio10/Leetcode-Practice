def binary(arr, n):
    low=0
    high=n-1
    if n==1:
        return arr[0]
    while low<=high:
        if arr[low]==arr[low+1]:
            low+=2
        else:
            return arr[low]
        if arr[high]==arr[high-1]:
            high-=2
        else:
            return arr[high]
    return -1

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(binary(arr, n))