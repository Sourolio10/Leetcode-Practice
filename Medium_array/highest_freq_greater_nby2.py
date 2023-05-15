def freq(arr,n):
    c=0
    for i in range(n):
        if c== 0:
            c==1
            el = arr[i]
        elif el == arr[i]:
            c+=1
        else:
            c-=1
    c2=0
    for i in range(n):
        if el == arr[i]:
            c2+=1
    if c2> n//2:
        return el
    else:
        return -1


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(freq(arr,n))