def binary1(arr, n,x):
    first = 0
    last =n-1
    mid = (first+last)//2
    while first < last:
        if arr[mid]< x:
            first +=1
            mid = (first+last)//2
        elif arr[mid]> x:
            last-=1
            mid = (first+last)//2
        else:
            return mid
            
    return -1

def binary(arr, n,x):
    m = binary1(arr, n,x)
    if m == -1:
        return 0
    k=1
    left = m-1
    right = m+1
    while left>=0 and arr[left]==x:
        k+=1
        left-=1
    while right <n and arr[right]==x:
        k+=1
        right+=1
    return k


#Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    x = int(input())
    n = len(arr)
    print(binary(arr, n,x))