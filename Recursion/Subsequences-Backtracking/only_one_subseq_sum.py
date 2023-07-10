def all_sub_sum(i,d,sum,s,arr,n):
    if i==n:
        if sum==s:
            print(d)
            return True
        return False
        
    d.append(arr[i])
    sum+=arr[i]

    if all_sub_sum(i+1,d,sum,s,arr,n) == True:
        return True


    d.pop()
    sum-=arr[i]

    if all_sub_sum(i+1,d,sum,s,arr,n) == True:
        return True
    return False

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    s = int(input())
    d =[]
    all_sub_sum(0,d,0,s,arr,n)