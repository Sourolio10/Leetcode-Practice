def all_sub_sum(i,d,s,arr,n):
    if i==n:
        if s==0:
            print(d)
        return
    if arr[i] <= s:    
        d.append(arr[i])

        all_sub_sum(i,d,s-arr[i],arr,n)


        d.pop()
    all_sub_sum(i+1,d,s,arr,n)

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    s = int(input())
    d =[]
    all_sub_sum(0,d,s,arr,n)