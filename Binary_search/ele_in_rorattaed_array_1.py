def binary(arr, n,x):
    first = 0
    last =n-1
    while first <= last:
        mid = (first+last)>>1
        if arr[mid] == x:
            return mid
        if arr[first] <= arr[mid]:
            if arr[first] <= x and arr[mid]>= x:
                last = mid-1
            else:
                first = mid+1
        else:
            if arr[mid]<=x and x<=arr[last]:
                first = mid+1
            else:
                last = mid-1

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    x = int(input())
    n = len(arr)
    print(binary(arr, n,x))