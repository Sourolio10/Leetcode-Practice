def twosum(arr,k,n):
    s ={}
    for i in range(n):
        rem = k - arr[i]
        if rem in s:
            return "YES"
        s[arr[i]] = i
    return "NO"

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    k = int(input())
    n = len(arr)
    print(twosum(arr,k,n))