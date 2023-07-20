from collections import defaultdict

def diff_int_sub(arr, n, k):
    r=l=0
    map = defaultdict(int)
    ans =0
    for r in range(n):
        map[arr[r]]+=1
        while len(map)> k:
            map[arr[l]]-=1
            if map[arr[l]]==0:
                del map[arr[l]]
            l+=1
        ans+= r-l+1
    return ans



# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    k = int(input())
    print(diff_int_sub(arr, n, k) - diff_int_sub(arr, n, k-1))