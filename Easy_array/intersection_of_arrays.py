def intersect(arr,n, arr2, n2):
    inter = []
    i=j=0
    while i< n and j< n2:
        if arr[i]< arr2[j]:
            i+=1
        elif arr[i] > arr2[j]:
            j+=1
        else:
            inter.append(arr[i])
            i+=1
            j+=1
    return inter

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr2=[]
    arr = [int(item) for item in input().split(',')]
    arr2 = [int(item) for item in input().split(',')]
    n = len(arr)
    n2= len(arr2)
    inter =[]
    inter = intersect(arr,n, arr2, n2)
    print(inter)