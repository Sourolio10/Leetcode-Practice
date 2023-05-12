def sort(arr,n):
    for i in range(0,n):
        j=i
        while j>0 and arr[j-1]> arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(sort(arr,n))