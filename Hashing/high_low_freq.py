def freq(arr,n):
    f = dict()
    for i in range(n):
        if arr[i] in f.keys():
            f[arr[i]]+=1
        else:
            f[arr[i]] = 1
    max=0
    min = 99999
    for k, v in f.items():
        
        if v>max:
            max = k
        if v< min:
            min = k

    return max,min

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(freq(arr,n))