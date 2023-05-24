def prod(arr, n):
    p=1
    zero = False
    maxL=maxR= arr[0]
    for i in arr:
        p*=i
        if i == 0:
            zero = True
            p =1
            continue
        maxL = max(maxL, p)
    
    p=1
    for i in range(n-1,0,-1):
        p*= arr[i]
        if arr[i] == 0:
            zero = True
            p =1
            continue
        maxR = max(maxR, p)

    if zero:
        return max(max(maxL, maxR),0)
    else:
        return max(maxL, maxR)
        

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(prod(arr, n))