def binary(arr, n,x):
    first = 0
    last =n-1
    pos=[]
    mid = (first+last)//2
    min_f_pos = n-1
    max_l_pos = 0
    while first < last:
        if arr[mid]< x:
            first +=1
            mid = (first+last)//2
        elif arr[mid]> x:
            last-=1
            mid = (first+last)//2
        else:
            if mid < min_f_pos:
                min_f_pos = mid
                mid-=1
            else:
                max_l_pos = mid
                mid+=1

    return min_f_pos+1,max_l_pos+1

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    x = int(input())
    n = len(arr)
    print(binary(arr, n,x))