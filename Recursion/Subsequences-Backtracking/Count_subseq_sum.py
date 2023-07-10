def all_sub_sum(i,d,sum,s,arr,n):
    if i==n:
        if sum==s:
            return 1

        return 0
        
    d.append(arr[i])
    sum+=arr[i]

    l = all_sub_sum(i+1,d,sum,s,arr,n)


    d.pop()
    sum-=arr[i]

    r = all_sub_sum(i+1,d,sum,s,arr,n)

    return l+r

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    s = int(input())
    d =[]
    print(all_sub_sum(0,d,0,s,arr,n))