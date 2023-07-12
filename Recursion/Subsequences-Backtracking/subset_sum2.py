
def helper(arr,n):
    sum1=[]
    d=[]
    arr.sort()
    def all_sub_sum(ind,d,sum1):
        sum1.append(d[:])
        for i in range(ind, n):
            if i != ind and arr[i] == arr[i - 1]:
                continue   
            d.append(arr[i])
            all_sub_sum(i+1,d,sum1)
            d.pop()
    all_sub_sum(0,d,sum1)
    return sum1
# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    x = helper(arr,n)
    print(*x)