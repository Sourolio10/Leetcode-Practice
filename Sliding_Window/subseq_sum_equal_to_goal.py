
def greater_than_k(arr,k):
    l=0
    sum=0
    count =0
    for r in range(len(arr)):
        sum+= arr[r]
        while l<=r and sum > k:
            count += n - r
            sum-= arr[l]
            l+=1
    return count

def less_than_k(arr,k):
    l=0
    sum=0
    count =0
    for r in range(len(arr)):
        sum+= arr[r]
        while l<=r and sum >= k:
            sum-= arr[l]
            l+=1
        count+= r-l+1
    return count    


if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    k= int(input())
    n = len(arr)
    print((n*(n+1)//2) - less_than_k(arr,k) - greater_than_k(arr,k))