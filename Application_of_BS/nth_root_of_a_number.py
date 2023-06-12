def multiply(mid,n):
    mul=1
    for i in range(1,n+1):
        mul*=mid
    return mul

def root(n,m):
    l=0
    h=m
    eps = 1e-7
    while h-l > eps:
        mid = (l+h)/2.0
        if multiply(mid,n) < m:
            l = mid
        else:
            h = mid
    return l


# Driver Code
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(root(n,m))