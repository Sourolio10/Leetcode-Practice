def sum4(arr,n,x):
    s=0
    t = set()
    for i in range(n):
        hashset = set()
        for j in range(i+1,n):
            for k in range(j+1,n):
                s= arr[i] + arr[j] + arr[k]
                fourth = x-s
                if fourth in hashset:
                    temp = [arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    t.add(tuple(temp))
                hashset.add(arr[k])

    return t

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    x = int(input())
    print(sum4(arr,n,x))