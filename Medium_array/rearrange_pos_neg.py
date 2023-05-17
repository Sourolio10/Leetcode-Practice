def rearr(arr,n):
    pos=[]
    neg=[]
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(len(pos)):
        arr[2*i]= pos[i]
    for i in range(len(neg)):
        arr[2*i+1]= neg[i]
    return arr
# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(rearr(arr,n))