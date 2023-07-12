
def helper(arr,n):
    sum1=[]
    d=[]
    def all_sub_sum(i,d,sum1):
        if i==n:
            sum1.append(sum(d))
            return
            
        d.append(arr[i])
        all_sub_sum(i+1,d,sum1)


        d.pop()

        all_sub_sum(i+1,d,sum1)
    all_sub_sum(0,d,sum1)
    return sorted(sum1)
# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    print(helper(arr,n))