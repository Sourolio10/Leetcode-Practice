def uniquePaths(m,n):
    N = m+n-2
    r = m-1
    res= 1
    for i in range(1, r+1):
        res*= (N-r+i)/i

    return int(res)

if __name__ == "__main__":
    m= int(input())
    n= int(input())
    totalCount = uniquePaths(m,n)
    print("The total number of Unique Paths are ", totalCount)