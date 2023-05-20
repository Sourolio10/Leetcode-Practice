from collections import defaultdict
def subxor(arr,n,x):
    x1 = 0
    d=defaultdict(int)
    c=0
    d[x1]=1
    for i in range(n):
        x1=x1^arr[i]
        k = x1^x
        c+=d[k]
        d[x1]+=1
    return c


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    x = int(input())
    print(subxor(arr,n,x))