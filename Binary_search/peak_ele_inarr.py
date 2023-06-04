def binary(arr, n):
    first = 0
    last =n-1
    while first < last:
        mid = (first+last)//2
        if mid==0:
            return max(arr[mid],arr[mid+1])
        if mid == n-1:
            return max(arr[mid],arr[mid-1])
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        if arr[mid] < arr[mid-1]:
            last= mid -1
        else:
            first=mid+1
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(binary(arr, n))