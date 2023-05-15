import sys
def stock(arr,n):
    minp= sys.maxsize
    maxp=0
    for i in range(n):
        minp = min(minp, arr[i])
        maxp = max(maxp, arr[i] - minp)
    return maxp
        


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(stock(arr,n))