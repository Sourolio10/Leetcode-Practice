import math
def binary(arr, h):
    l,h=1,max(arr)
    while l<h:
        mid = (l+h)//2
        tot = 0
        tot = sum(math.ceil(p/mid) for p in arr)
        if tot > h:
            l= mid+1
        else:
            h = mid
    return l
            

if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = int(input())
    print(binary(arr, n))