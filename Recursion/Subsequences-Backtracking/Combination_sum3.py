def all_sub_sum(i,d,sum,s,arr,n,k):
    if i==n:
        if len(d) == k:
            if sum==s:
                print(d)
        return
        
    d.append(arr[i])
    sum+=arr[i]

    all_sub_sum(i+1,d,sum,s,arr,n,k)


    d.pop()
    sum-=arr[i]

    all_sub_sum(i+1,d,sum,s,arr,n,k)

# Driver Code
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    n= len(arr)
    s = int(input())
    k = int(input())
    d =[]
    if k>s:
        print([])
    else:
        all_sub_sum(0,d,0,s,arr,n,k)