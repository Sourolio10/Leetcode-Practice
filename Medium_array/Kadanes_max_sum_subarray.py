import sys
def kadane(arr,n):
    max = -sys.maxsize-1
    s=0
    for i in range(n):
        s+=arr[i]
        
        if s> max:
            max=s
        if s<0:
            s=0
    return max

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(kadane(arr,n))