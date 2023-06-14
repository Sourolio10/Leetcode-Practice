def arrangecow(arr,n,mid, cows):
    c=1
    cow_placed = arr[0]
    for i in range(1, n):
        if arr[i] -  cow_placed >= mid:
            c+=1
            cow_placed = arr[i]

    if c>=cows:
        return True
    else:
        return False


def binary(arr, n, cows):
    low = 1
    high = arr[n-1] - arr[0]
    while low<=high:
        mid = (low+high)//2
        if arrangecow(arr,n,mid, cows):
            low = mid +1
        else:
            high = mid - 1
    return high

if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n=len(arr)
    cows = int(input())
    print(binary(arr, n, cows))