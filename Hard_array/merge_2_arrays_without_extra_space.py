def merge(arr1, arr2, n, m):

    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()

# Driver Code
if __name__ == "__main__":
    arr1=[]
    arr2=[]
    arr1 = [int(item) for item in input().split(',')]
    arr2 = [int(item) for item in input().split(',')]
    n = len(arr1)
    m = len(arr2)
    merge(arr1, arr2, n, m)
    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()