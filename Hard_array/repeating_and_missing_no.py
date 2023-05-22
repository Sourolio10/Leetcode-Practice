def rnp(arr,n):
    h=[0]*(n+1)

    for i in range(n):
        h[arr[i]]+=1

    miss,repeat = -1,-1
    for i in range(1,n+1):
        if h[i] >1:
            repeat = i
        if h[i] == 0:
            miss = i
        if repeat!=-1 and miss!=-1:
            break
    return [repeat, miss]

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(rnp(arr,n))