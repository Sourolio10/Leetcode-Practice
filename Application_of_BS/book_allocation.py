def books_alloc(arr,n,m,mid):
    c=1
    ps=0
    for i in arr:
        if ps+i<=mid:
            ps+=i
        else:
            c+=1
            if c>m or  i>mid:
                return False
            ps=i
    return True
        
def binary(arr, n, m):
    low=0
    high = sum(arr)
    ans = -1
    while low<= high:
        mid = (low+high)//2
        if books_alloc(arr,n,m,mid):
            ans = mid
            high= mid-1
        else:
            low = mid+1
    return ans

if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    m = int(input())
    n = len(arr)
    print(binary(arr, n, m))