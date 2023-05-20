def sum3(arr,n,x):
    s=0
    t = set()
    for i in range(n):
        hashset = set()
        for j in range(i+1,n):
                s= arr[i] + arr[j]
                third = x-s
                if third in hashset:
                    temp = [arr[i],arr[j],third]
                    temp.sort()
                    t.add(tuple(temp))
                hashset.add(arr[j])

    return t

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    x = int(input())
    print(sum3(arr,n,x))