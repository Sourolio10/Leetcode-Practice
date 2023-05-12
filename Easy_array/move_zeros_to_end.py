def zeros(arr,n):
    k=n
    for i in range(n):
        if arr[i]==0:
            k=i
            break
    if k!=n:
        i=k
        j=k+1
        while j<n and i<n:
            if arr[j]!=0:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
            j+=1


# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    zeros(arr,n)
    print(arr)