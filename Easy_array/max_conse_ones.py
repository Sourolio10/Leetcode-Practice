def ones(arr,n):
    c=0
    max = 0
    for i in range(n):
        if arr[i] == 1:
            c+=1
        else:
            c=0
        if c > max:
            max = c
    return max


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    max = ones(arr,n)
    print(max)