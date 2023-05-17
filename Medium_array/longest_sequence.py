def seq(arr, n):
    hash= set()
    for i in arr:
        hash.add(i)
    long_seq = 0
    for i in arr:
        if i-1 not in hash:
            curr_ele = i
            curr_seq =1
            while curr_ele + 1 in hash:
                curr_ele+=1
                curr_seq+=1
            
            long_seq =  max(long_seq,curr_seq)
    return long_seq

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n = len(arr)
    print(seq(arr, n))