from math import ceil
def binary(arr, n,x):
    f,l=max(arr), sum(arr)
    def check(m):
        s=1
        max = m
        for i in arr:
            if i > max:
                max = m
                s+=1
            max-=i
        return True if s<=x else False
    
    while f<l:
        m= (f+l)//2
        if check(m):
            l=m
        else:
            f=m+1
    return f



#Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    x = int(input())
    n = len(arr)
    print(binary(arr, n,x))