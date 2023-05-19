def freq(arr,n):
    d={}
    l=[]
    mini = n//3+1
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1
        
        if d[arr[i]] >= mini:
            l.append(arr[i])
    return l

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(freq(arr,n))