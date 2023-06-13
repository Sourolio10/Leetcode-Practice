from math import ceil
def binary(arr, n,x):
    f,l=1, max(arr)+1
    def check(m):
        s=0
        for i in arr:
            s+= ceil(i/m)
        return s<=x
    
    while f<l:
        m= (f+l)//2
        if check(m):
            ans = m
            l=m
        else:
            f=m+1
    return ans



#Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    x = int(input())
    n = len(arr)
    print(binary(arr, n,x))