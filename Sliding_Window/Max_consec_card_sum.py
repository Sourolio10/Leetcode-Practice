def k_consec_sum(arr, k, n):
    rem = n-k
    sum1 = sum(arr[:rem])
    minsum= sum1
    for i in range(rem, n):
        sum1+= arr[i]
        sum1-= arr[i]
        minsum = min(minsum, sum1)

    return sum(arr) - minsum



if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    k = int(input())
    print(k_consec_sum(arr, k, n))