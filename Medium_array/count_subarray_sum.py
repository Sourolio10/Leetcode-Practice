from collections import defaultdict
def subsum(arr,n,x):
    psum = 0
    d=defaultdict(int)
    c=0
    d[0]=1
    for i in range(n):
        psum+=arr[i]
        rem = psum - x
        c+=d[rem]
        d[psum]+=1
    return c


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    x = int(input())
    print(subsum(arr,n,x))