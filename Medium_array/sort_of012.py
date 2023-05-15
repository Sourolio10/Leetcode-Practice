
def sort(arr,n):
    low =0
    high = n-1
    mid = 0
    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]= arr[mid],arr[low]
            low+=1
            mid+=1

        elif arr[mid]==2:
            arr[high],arr[mid]= arr[mid],arr[high]
            high-=1
        else:
            mid+=1
    return arr
    
        

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(sort(arr,n))
