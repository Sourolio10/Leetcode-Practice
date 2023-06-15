def median(arr1, arr2,  n, m):
    if m>n:
        return median(arr2, arr1,  m,n)
    low =0
    high = n
    medianp = (n+m+1)//2
    while low<=high:
        cut1 = (low+high)//2
        cut2 = medianp - cut1

        l1 = float('-inf') if cut1 ==0 else arr1[cut1-1]
        l2 = float('-inf') if cut2 ==0 else arr2[cut2-1]
        r1 = float('inf') if cut1 ==n else arr1[cut1]
        r2 = float('inf') if cut2 ==m else arr2[cut2]

        if l1<=r2 and l2<=r1:
            if (m+n)%2 ==1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1,r2))/2.0
        elif l1 > r2:
            high = cut1 -1
        else:
            low = cut1+1
    return 0.0

if __name__ == "__main__":
    arr1=[]
    arr2=[]
    arr1 = [int(item) for item in input().split(',')]
    arr2 = [int(item) for item in input().split(',')]
    m = len(arr2)
    n = len(arr1)
    print(median(arr1, arr2,  n, m))