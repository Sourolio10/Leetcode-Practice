def gas_stat_possible(arr,n,m,mid):
    no_gas_stat = 0
    for i in range(1, n):
        no_gas_stat+= (arr[i] - arr[i-1])//mid
    return no_gas_stat <= m

def binary(arr, n, m):
    low=0
    high = arr[-1] - arr[0]
    while high - low > 1e-7:
        mid = (low+high)/2
        if gas_stat_possible(arr,n,m,mid):
            high= mid
        else:
            low = mid
    return high

if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    m = int(input())
    n = len(arr)
    print(binary(arr, n, m))