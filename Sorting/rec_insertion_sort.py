def sort(arr,n,i,j):
    if i==n:
        return
    
    if j>0 and arr[j-1] > arr[j]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        sort(arr,n,i,j-1)
    sort(arr,n,i+1,i+1)

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    sort(arr,n,0,0)
    print(arr)