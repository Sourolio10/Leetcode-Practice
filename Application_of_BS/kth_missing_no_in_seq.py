def binary(arr, n, k):
        start, end = 0, n-1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k


if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    k= int(input())
    n = len(arr)
    print(binary(arr, n, k))