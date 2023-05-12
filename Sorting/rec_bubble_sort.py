def sort(arr,n,i,j):
    if i==n-1 or j ==n-1:
        j=0
        return
    
    if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
    sort(arr,n,i,j+1)
    sort(arr,n,i+1,j)

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    sort(arr,n,0,0)
    print(arr)