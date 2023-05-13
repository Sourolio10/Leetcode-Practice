def freq(arr,n):
    f = dict()
    for i in range(n):
        if arr[i] in f.keys():
            f[arr[i]]+=1
        else:
            f[arr[i]] = 1
    return f

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    f = freq(arr,n)
    for k, v in f.items():
        if v == 1:
            print(k)
            break